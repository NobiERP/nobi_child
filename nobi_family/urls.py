# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'nobi_family'
urlpatterns = [
    url(
        regex="^Child/~create/$",
        view=views.ChildCreateView.as_view(),
        name='Child_create',
    ),
    url(
        regex="^Child/(?P<pk>\d+)/~delete/$",
        view=views.ChildDeleteView.as_view(),
        name='Child_delete',
    ),
    url(
        regex="^Child/(?P<pk>\d+)/$",
        view=views.ChildDetailView.as_view(),
        name='Child_detail',
    ),
    url(
        regex="^Child/(?P<pk>\d+)/~update/$",
        view=views.ChildUpdateView.as_view(),
        name='Child_update',
    ),
    url(
        regex="^Child/$",
        view=views.ChildListView.as_view(),
        name='Child_list',
    ),
	]
