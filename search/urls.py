"""
Urls for search management

These are linked at /search/
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sector/incomplete/$', views.sector_search_incomplete, name='sector_search_incomplete'),
    url(r'^sector/incomplete/kml/$', views.sector_search_incomplete_kml, name='sector_search_incomplete_kml'),
    url(r'^sector/completed/$', views.sector_search_completed, name='sector_search_completed'),
    url(r'^sector/completed/kml/$', views.sector_search_completed_kml, name='sector_search_completed_kml'),
    url(r'^sector/create/$', views.sector_search_create, name='sector_search_create'),
    url(r'^sector/(?P<search_id>\d+)/json/$', views.sector_search_json, name='sector_search_json'),
    url(r'^sector/(?P<search_id>\d+)/begin/$', views.sector_search_begin, name='sector_search_begin'),
    url(r'^sector/(?P<search_id>\d+)/finished/$', views.sector_search_finished, name='sector_search_finished'),
    url(r'^expandingbox/incomplete/$', views.expanding_box_search_incomplete, name='expanding_box_search_incomplete'),
    url(r'^expandingbox/incomplete/kml/$', views.expanding_box_search_incomplete_kml, name='expanding_box_search_incomplete_kml'),
    url(r'^expandingbox/completed/$', views.expanding_box_search_completed, name='expanding_box_search_completed'),
    url(r'^expandingbox/completed/kml/$', views.expanding_box_search_completed_kml, name='expanding_box_search_completed_kml'),
    url(r'^expandingbox/create/$', views.expanding_box_search_create, name='expanding_box_search_create'),
    url(r'^expandingbox/(?P<search_id>\d+)/json/$', views.expanding_box_search_json, name='expanding_box_search_json'),
    url(r'^expandingbox/(?P<search_id>\d+)/begin/$', views.expanding_box_search_begin, name='expanding_box_search_begin'),
    url(r'^expandingbox/(?P<search_id>\d+)/finished/$', views.expanding_box_search_finished, name='expanding_box_search_finished'),
    url(r'^trackline/incomplete/$', views.track_line_search_incomplete, name='track_line_search_incomplete'),
    url(r'^trackline/incomplete/kml/$', views.track_line_search_incomplete_kml, name='track_line_search_incomplete_kml'),
    url(r'^trackline/completed/$', views.track_line_search_completed, name='track_line_search_completed'),
    url(r'^trackline/completed/kml/$', views.track_line_search_completed_kml, name='track_line_search_completed_kml'),
    url(r'^trackline/create/$', views.track_line_search_create, name='track_line_search_create'),
    url(r'^trackline/(?P<search_id>\d+)/json/$', views.track_line_search_json, name='track_line_search_json'),
    url(r'^trackline/(?P<search_id>\d+)/begin/$', views.track_line_search_begin, name='track_line_search_begin'),
    url(r'^trackline/(?P<search_id>\d+)/finished/$', views.track_line_search_finished, name='track_line_search_finished'),
    url(r'^creepingline/track/incomplete/$', views.creeping_line_track_search_incomplete, name='creeping_line_track_search_incomplete'),
    url(r'^creepingline/track/incomplete/kml/$', views.creeping_line_track_search_incomplete_kml, name='creeping_line_track_search_incomplete_kml'),
    url(r'^creepingline/track/completed/$', views.creeping_line_track_search_completed, name='creeping_line_track_search_completed'),
    url(r'^creepingline/track/completed/kml/$', views.creeping_line_track_search_completed_kml, name='creeping_line_track_search_completed_kml'),
    url(r'^creepingline/create/track/$', views.track_creeping_line_search_create, name='track_creeping_line_search_create'),
    url(r'^creepingline/track/(?P<search_id>\d+)/json/$', views.creeping_line_track_search_json, name='creeping_line_track_search_json'),
    url(r'^creepingline/track/(?P<search_id>\d+)/begin/$', views.creeping_line_track_search_begin, name='creeping_line_track_search_begin'),
    url(r'^creepingline/track/(?P<search_id>\d+)/finished/$', views.creeping_line_track_search_finished, name='creeping_line_track_search_finished'),
    url(r'^creepingline/polygon/incomplete/$', views.creeping_line_polygon_search_incomplete, name='creeping_line_polygon_search_incomplete'),
    url(r'^creepingline/polygon/incomplete/kml/$', views.creeping_line_polygon_search_incomplete_kml, name='creeping_line_polygon_search_incomplete_kml'),
    url(r'^creepingline/polygon/completed/$', views.creeping_line_polygon_search_completed, name='creeping_line_polygon_search_completed'),
    url(r'^creepingline/polygon/completed/kml/$', views.creeping_line_polygon_search_completed_kml, name='creeping_line_polygon_search_completed_kml'),
    url(r'^creepingline/create/polygon/$', views.polygon_creeping_line_search_create, name='polygon_creeping_line_search_create'),
    url(r'^creepingline/polygon/(?P<search_id>\d+)/json/$', views.creeping_line_polygon_search_json, name='creeping_line_polygon_search_json'),
    url(r'^creepingline/polygon/(?P<search_id>\d+)/begin/$', views.creeping_line_polygon_search_begin, name='creeping_line_polygon_search_begin'),
    url(r'^creepingline/polygon/(?P<search_id>\d+)/finished/$', views.creeping_line_polygon_search_finished, name='creeping_line_polygon_search_finished'),
    url(r'^find/closest/$', views.find_closest_search, name='find_closest_search'),
]
