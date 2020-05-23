"""
Urls for search management

These are linked at /search/
"""
from django.conf.urls import url
from . import views, view_helpers
from .models import SectorSearch, ExpandingBoxSearch, TrackLineSearch, TrackLineCreepingSearch, PolygonSearch

urlpatterns = [
    url(r'^mission/(?P<mission_id>\d+)/search/sector/incomplete/$', views.search_incomplete, {'search_class': SectorSearch}, name='sector_search_incomplete'),
    url(r'^mission/(?P<mission_id>\d+)/search/sector/incomplete/kml/$', views.search_incomplete_kml, {'search_class': SectorSearch}, name='sector_search_incomplete_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/sector/completed/$', views.search_completed, {'search_class': SectorSearch}, name='sector_search_completed'),
    url(r'^mission/(?P<mission_id>\d+)/search/sector/completed/kml/$', views.search_completed_kml, {'search_class': SectorSearch}, name='sector_search_completed_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/sector/(?P<search_id>\d+)/queue/for/asset/$', views.search_queue_for_asset, {'object_class': SectorSearch}, name='sector_search_queue_for_asset'),
    url(r'^mission/(?P<mission_id>\d+)/search/sector/(?P<search_id>\d+)/queue/for/assettype/$', views.search_queue_for_asset_type, {'object_class': SectorSearch}, name='sector_search_queue_for_assetype'),
    url(r'^search/sector/create/$', views.sector_search_create, name='sector_search_create'),
    url(r'^search/sector/(?P<search_id>\d+)/json/$', view_helpers.search_json, {'object_class': SectorSearch}, name='sector_search_json'),
    url(r'^search/sector/(?P<search_id>\d+)/begin/$', views.search_begin, {'object_class': SectorSearch}, name='sector_search_begin'),
    url(r'^search/sector/(?P<search_id>\d+)/finished/$', views.search_finished, {'object_class': SectorSearch}, name='sector_search_finished'),
    url(r'^mission/(?P<mission_id>\d+)/search/expandingbox/incomplete/$', views.search_incomplete, {'search_class': ExpandingBoxSearch}, name='expanding_box_search_incomplete'),
    url(r'^mission/(?P<mission_id>\d+)/search/expandingbox/incomplete/kml/$', views.search_incomplete_kml, {'search_class': ExpandingBoxSearch}, name='expanding_box_search_incomplete_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/expandingbox/completed/$', views.search_completed, {'search_class': ExpandingBoxSearch}, name='expanding_box_search_completed'),
    url(r'^mission/(?P<mission_id>\d+)/search/expandingbox/completed/kml/$', views.search_completed_kml, {'search_class': ExpandingBoxSearch}, name='expanding_box_search_completed_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/expandingbox/(?P<search_id>\d+)/queue/for/asset/$', views.search_queue_for_asset, {'object_class': ExpandingBoxSearch}, name='expanding_box_search_queue_for_asset'),
    url(r'^mission/(?P<mission_id>\d+)/search/expandingbox/(?P<search_id>\d+)/queue/for/assettype/$', views.search_queue_for_asset_type, {'object_class': ExpandingBoxSearch}, name='expanding_box_search_queue_for_assetype'),
    url(r'^search/expandingbox/create/$', views.expanding_box_search_create, name='expanding_box_search_create'),
    url(r'^search/expandingbox/(?P<search_id>\d+)/json/$', view_helpers.search_json, {'object_class': ExpandingBoxSearch}, name='expanding_box_search_json'),
    url(r'^search/expandingbox/(?P<search_id>\d+)/begin/$', views.search_begin, {'object_class': ExpandingBoxSearch}, name='expanding_box_search_begin'),
    url(r'^search/expandingbox/(?P<search_id>\d+)/finished/$', views.search_finished, {'object_class': ExpandingBoxSearch}, name='expanding_box_search_finished'),
    url(r'^mission/(?P<mission_id>\d+)/search/trackline/incomplete/$', views.search_incomplete, {'search_class': TrackLineSearch}, name='track_line_search_incomplete'),
    url(r'^mission/(?P<mission_id>\d+)/search/trackline/incomplete/kml/$', views.search_incomplete_kml, {'search_class': TrackLineSearch}, name='track_line_search_incomplete_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/trackline/completed/$', views.search_completed, {'search_class': TrackLineSearch}, name='track_line_search_completed'),
    url(r'^mission/(?P<mission_id>\d+)/search/trackline/completed/kml/$', views.search_completed_kml, {'search_class': TrackLineSearch}, name='track_line_search_completed_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/trackline/(?P<search_id>\d+)/queue/for/asset/$', views.search_queue_for_asset, {'object_class': TrackLineSearch}, name='track_line_search_queue_for_asset'),
    url(r'^mission/(?P<mission_id>\d+)/search/trackline/(?P<search_id>\d+)/queue/for/assettype/$', views.search_queue_for_asset_type, {'object_class': TrackLineSearch}, name='track_line_search_queue_for_assetype'),
    url(r'^search/trackline/create/$', views.track_line_search_create, name='track_line_search_create'),
    url(r'^search/trackline/(?P<search_id>\d+)/json/$', view_helpers.search_json, {'object_class': TrackLineSearch}, name='track_line_search_json'),
    url(r'^search/trackline/(?P<search_id>\d+)/begin/$', views.search_begin, {'object_class': TrackLineSearch}, name='track_line_search_begin'),
    url(r'^search/trackline/(?P<search_id>\d+)/finished/$', views.search_finished, {'object_class': TrackLineSearch}, name='track_line_search_finished'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/track/incomplete/$', views.search_incomplete, {'search_class': TrackLineCreepingSearch}, name='creeping_line_track_search_incomplete'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/track/incomplete/kml/$', views.search_incomplete_kml, {'search_class': TrackLineCreepingSearch}, name='creeping_line_track_search_incomplete_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/track/completed/$', views.search_completed, {'search_class': TrackLineCreepingSearch}, name='creeping_line_track_search_completed'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/track/completed/kml/$', views.search_completed_kml, {'search_class': TrackLineCreepingSearch}, name='creeping_line_track_search_completed_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/track/(?P<search_id>\d+)/queue/for/asset/$', views.search_queue_for_asset, {'object_class': TrackLineCreepingSearch}, name='creeping_line_search_queue_for_asset'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/track/(?P<search_id>\d+)/queue/for/assettype/$', views.search_queue_for_asset_type, {'object_class': TrackLineCreepingSearch}, name='creeping_line_search_queue_for_assetype'),
    url(r'^search/creepingline/create/track/$', views.track_creeping_line_search_create, name='track_creeping_line_search_create'),
    url(r'^search/creepingline/track/(?P<search_id>\d+)/json/$', view_helpers.search_json, {'object_class': TrackLineCreepingSearch}, name='creeping_line_track_search_json'),
    url(r'^search/creepingline/track/(?P<search_id>\d+)/begin/$', views.search_begin, {'object_class': TrackLineCreepingSearch}, name='creeping_line_track_search_begin'),
    url(r'^search/creepingline/track/(?P<search_id>\d+)/finished/$', views.search_finished, {'object_class': TrackLineCreepingSearch}, name='creeping_line_track_search_finished'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/polygon/incomplete/$', views.search_incomplete, {'search_class': PolygonSearch}, name='creeping_line_polygon_search_incomplete'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/polygon/incomplete/kml/$', views.search_incomplete_kml, {'search_class': PolygonSearch}, name='creeping_line_polygon_search_incomplete_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/polygon/completed/$', views.search_completed, {'search_class': PolygonSearch}, name='creeping_line_polygon_search_completed'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/polygon/completed/kml/$', views.search_completed_kml, {'search_class': PolygonSearch}, name='creeping_line_polygon_search_completed_kml'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingling/polygon/(?P<search_id>\d+)/queue/for/asset/$', views.search_queue_for_asset, {'object_class': PolygonSearch}, name='creeping_line_polygon_search_queue_for_asset'),
    url(r'^mission/(?P<mission_id>\d+)/search/creepingline/polygon/(?P<search_id>\d+)/queue/for/assettype/$', views.search_queue_for_asset_type, {'object_class': PolygonSearch}, name='creeping_line_polygon_search_queue_for_assetype'),
    url(r'^search/creepingline/create/polygon/$', views.polygon_creeping_line_search_create, name='polygon_creeping_line_search_create'),
    url(r'^search/creepingline/polygon/(?P<search_id>\d+)/json/$', view_helpers.search_json, {'object_class': PolygonSearch}, name='creeping_line_polygon_search_json'),
    url(r'^search/creepingline/polygon/(?P<search_id>\d+)/begin/$', views.search_begin, {'object_class': PolygonSearch}, name='creeping_line_polygon_search_begin'),
    url(r'^search/creepingline/polygon/(?P<search_id>\d+)/finished/$', views.search_finished, {'object_class': PolygonSearch}, name='creeping_line_polygon_search_finished'),
    url(r'^search/find/closest/$', views.find_next_search, name='find_next_search'),
]
