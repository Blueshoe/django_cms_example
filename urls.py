# -*- coding: utf-8 -*-

from django.conf.urls import *

from showroom.views import CategoryListView, ArtPieceListView

urlpatterns = patterns('showroom.views',
    url(r'^$', CategoryListView.as_view(), name='category_list'),
    url(r'^artpiece/(?P<cat_id>\d+)/$', ArtPieceListView.as_view(), name='artpiece_list'),
)