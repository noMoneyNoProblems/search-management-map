"""
Mission Create/Management Views.
"""

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseForbidden
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie

from assets.models import Asset, AssetCommand
from timeline.models import TimeLineEntry
from timeline.helpers import timeline_record_create, timeline_record_mission_user_add, timeline_record_mission_user_update, timeline_record_mission_asset_add, timeline_record_mission_asset_remove

from .models import Mission, MissionUser, MissionAsset, MissionAssetType
from .forms import MissionForm, MissionUserForm, MissionAssetForm, MissionTimeLineEntryForm
from .decorators import mission_is_member, mission_is_admin


@login_required
@mission_is_member
def mission_details(request, mission_user):
    """
    Missions details and management.
    """
    data = {
        'mission': mission_user.mission,
        'me': request.user,
        'admin': mission_user.role == 'A',
        'mission_assets': MissionAsset.objects.filter(mission=mission_user.mission),
        'mission_users': MissionUser.objects.filter(mission=mission_user.mission),
        'mission_asset_types': MissionAssetType.objects.filter(mission=mission_user.mission),
        'mission_user_add': MissionUserForm(),
        'mission_asset_add': MissionAssetForm(),
    }
    return render(request, 'mission_details.html', data)


@login_required
@mission_is_member
def mission_timeline(request, mission_user):
    """
    Mission timeline, a history of everything that happened during a mission.
    """
    data = {
        'mission': mission_user.mission,
        'timeline': TimeLineEntry.objects.filter(mission=mission_user.mission).order_by('timestamp'),
    }
    return render(request, 'mission_timeline.html', data)


@login_required
@mission_is_admin
def mission_close(request, mission_user):
    """
    Close a Mission
    """
    if mission_user.mission.closed is not None:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    mission_user.mission.closed = timezone.now()
    mission_user.mission.closed_by = request.user
    mission_user.mission.save()

    # Tell all the assets, and free them from this mission
    assets = MissionAsset.objects.filter(mission=mission_user.mission, removed__isnull=True)
    for mission_asset in assets:
        command = AssetCommand(asset=mission_asset.asset, issued_by=mission_user.user, command='MC', reason='The Mission was Closed', mission=mission_user.mission)
        command.save()
        mission_asset.remover = request.user
        mission_asset.removed = timezone.now()
        mission_asset.save()
        timeline_record_mission_asset_remove(mission_user.mission, request.user, asset=mission_asset.asset)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
@ensure_csrf_cookie
def mission_list(request):
    """
    List missions this user can select from.
    """
    user_missions = MissionUser.objects.filter(user=request.user)
    current_missions = []
    previous_missions = []
    for user_mission in user_missions:
        if user_mission.role == 'A':
            user_mission.mission.is_admin = True
        if user_mission.mission.closed is not None:
            previous_missions.append(user_mission.mission)
        else:
            current_missions.append(user_mission.mission)

    data = {
        'current_missions': current_missions,
        'previous_missions': previous_missions,
    }

    return render(request, 'mission_list.html', data)


@login_required
def mission_new(request):
    """
    Create a new mission.
    """
    form = None
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            # Create the new mission
            mission = Mission(mission_name=form.cleaned_data['mission_name'], creator=request.user)
            mission.save()
            # Give the user who created this mission admin permissions
            MissionUser(mission=mission, user=request.user, role='A', creator=request.user).save()
            return redirect('/mission/{}/details/'.format(mission.pk))

    if form is None:
        form = MissionForm()

    return render(request, 'mission_create.html', {'form': form})


@login_required
@mission_is_member
def mission_timeline_add(request, mission_user):
    """
    Add a custom entry to the timeline for a mission.
    """
    form = None
    if request.method == 'POST':
        form = MissionTimeLineEntryForm(request.POST)
        if form.is_valid():
            entry = TimeLineEntry(mission=mission_user.mission, user=request.user, message=form.cleaned_data['message'], timestamp=form.cleaned_data['timestamp'], url=form.cleaned_data['url'], event_type='usr')
            entry.save()
            timeline_record_create(mission_user.mission, request.user, entry)
            return HttpResponseRedirect("/mission/{}/timeline/".format(mission_user.mission.pk))

    if form is None:
        form = MissionTimeLineEntryForm()

    return render(request, 'mission_timeline_add.html', {'form': form})


@login_required
@mission_is_admin
def mission_user_add(request, mission_user):
    """
    Add a User to a Mission
    """
    form = None
    if request.method == 'POST':
        form = MissionUserForm(request.POST)
        if form.is_valid():
            # Check if this user is already in this mission
            try:
                mission_user = MissionUser.objects.get(user=form.cleaned_data['user'], mission=mission_user.mission)
                return HttpResponseForbidden("User is already in this Mission")
            except ObjectDoesNotExist:
                # Create the new mission<->user
                mission_user = MissionUser(mission=mission_user.mission, user=form.cleaned_data['user'], creator=request.user)
                mission_user.save()
                timeline_record_mission_user_add(mission_user.mission, request.user, form.cleaned_data['user'])
                return HttpResponseRedirect('/mission/{}/details/'.format(mission_user.mission.pk))

    if form is None:
        form = MissionAssetForm()

    return render(request, 'mission_user_add.html', {'form': form})


@login_required
@mission_is_admin
def mission_user_make_admin(request, mission_user, user_id):
    """
    Make an existing user an admin for this mission.
    """
    # Find the User
    user = get_object_or_404(get_user_model(), pk=user_id)
    # Find the MissionUser
    mission_user_update = get_object_or_404(MissionUser, mission=mission_user.mission, user=user)
    mission_user_update.role = 'A'
    mission_user_update.save()
    timeline_record_mission_user_update(mission_user.mission, request.user, mission_user_update)
    return HttpResponseRedirect('/mission/{}/details/'.format(mission_user.mission.pk))


@login_required
@mission_is_admin
def mission_asset_add(request, mission_user):
    """
    Add an Asset to a Mission
    """
    form = None
    if request.method == 'POST':
        form = MissionAssetForm(request.POST)
        if form.is_valid():
            # Check if this asset is in any other missions currently
            try:
                mission_asset = MissionAsset.objects.get(asset=form.cleaned_data['asset'], removed__isnull=True)
                return HttpResponseForbidden("Asset is already in another Mission")
            except ObjectDoesNotExist:
                # Create the new mission<->asset
                mission_asset = MissionAsset(mission=mission_user.mission, asset=form.cleaned_data['asset'], creator=request.user)
                mission_asset.save()
                timeline_record_mission_asset_add(mission_user.mission, request.user, asset=form.cleaned_data['asset'])
                command = AssetCommand(asset=mission_asset.asset, issued_by=mission_user.user, command='RON', reason='Added to mission', mission=mission_user.mission)
                command.save()

                return HttpResponseRedirect('/mission/{}/details/'.format(mission_user.mission.pk))

    if form is None:
        form = MissionAssetForm()

    return render(request, 'mission_asset_add.html', {'form': form})


@login_required
@mission_is_member
def mission_asset_json(request, mission_user):
    """
    List Assets in a Mission
    """
    assets = MissionAsset.objects.filter(mission=mission_user.mission, removed__isnull=True)
    assets_json = []
    for mission_asset in assets:
        assets_json.append({
            'id': mission_asset.asset.pk,
            'name': mission_asset.asset.name,
            'type_id': mission_asset.asset.asset_type.id,
            'type_name': mission_asset.asset.asset_type.name,
        })
    data = {
        'assets': assets_json,
    }
    return JsonResponse(data)


@login_required
@mission_is_admin
def mission_asset_remove(request, mission_user, asset_id):
    """
    Cease using an asset as part of this Mission
    """
    asset = get_object_or_404(Asset, pk=asset_id)
    mission_asset = get_object_or_404(MissionAsset, mission=mission_user.mission, asset=asset, removed__isnull=True)
    mission_asset.remover = request.user
    mission_asset.removed = timezone.now()
    mission_asset.save()

    timeline_record_mission_asset_remove(mission_user.mission, request.user, asset=asset)

    # Tell the asset
    command = AssetCommand(asset=asset.asset, issued_by=mission_user.user, command='MC', reason='Removed from Mission', mission=mission_user.mission)
    command.save()

    return HttpResponseRedirect('/mission/{}/details/'.format(mission_user.mission.pk))
