# Generated by Django 3.0.6 on 2020-05-23 09:33

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mission', '0001_initial'),
        ('assets', '0003_assetcommand_mission'),
        ('data', '0019_auto_20200523_1816'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0016_auto_20200523_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo', django.contrib.gis.db.models.fields.GeometryField(geography=True, srid=4326)),
                ('alt', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('replaced_at', models.DateTimeField(blank=True, null=True)),
                ('sweep_width', models.IntegerField()),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('queued_at', models.DateTimeField(blank=True, null=True)),
                ('completed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='completed_bysearch_search_related', to='assets.Asset')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_bysearch_search_related', to=settings.AUTH_USER_MODEL)),
                ('created_for', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='assets.AssetType')),
                ('datum', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.GeoTimeLabel')),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='deletorsearch_search_related', to=settings.AUTH_USER_MODEL)),
                ('inprogress_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inprogress_bysearch_search_related', to='assets.Asset')),
                ('mission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mission.Mission')),
                ('queued_for_asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='queued_for_assettypesearch_search_related', to='assets.Asset')),
                ('queued_for_assettype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='queued_for_assettypesearch_search_related', to='assets.AssetType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='search',
            index=models.Index(fields=['mission', 'deleted_at', 'replaced_at', 'created_at', 'completed_at'], name='search_sear_mission_0ada99_idx'),
        ),
        migrations.AddIndex(
            model_name='search',
            index=models.Index(fields=['mission', 'deleted_at', 'replaced_at', 'completed_at'], name='search_sear_mission_1bad09_idx'),
        ),
        migrations.AddIndex(
            model_name='search',
            index=models.Index(fields=['mission', 'deleted_at', 'replaced_at', 'completed_at', 'inprogress_by'], name='search_sear_mission_0728ec_idx'),
        ),
        migrations.AddIndex(
            model_name='search',
            index=models.Index(fields=['mission', 'deleted_at', 'replaced_at', 'completed_at', 'inprogress_by', 'created_for'], name='search_sear_mission_f6254e_idx'),
        ),
        migrations.AddIndex(
            model_name='search',
            index=models.Index(fields=['mission', 'deleted_at', 'replaced_at', 'completed_at', 'inprogress_by', 'queued_for_asset', 'queued_for_assettype'], name='search_sear_mission_c76b3e_idx'),
        ),
    ]
