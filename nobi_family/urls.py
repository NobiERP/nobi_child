# -*- coding: utf-8 -*-
from django.urls import path, include

from . import views

app_name = 'nobi_family'
urlpatterns = [
    path("Person/", include([
        path(
            "",
            view=views.PersonListView.as_view(),
            name='Person_list',
        ),
        path(
            "~create/",
            view=views.PersonCreateView.as_view(),
            name='Person_create',
        ),
        path("<uuid:pk>/", include([
            path("",
                 view=views.PersonDetailView.as_view(),
                 name='Person_detail'
                 ),
            path(
                "~update/",
                view=views.PersonUpdateView.as_view(),
                name='Person_update',
            ),
            path(
                "~delete/",
                view=views.PersonDeleteView.as_view(),
                name='Person_delete',
            ),
        ])),
    ])),
    path("Language/", include([
        path(
            "",
            view=views.LanguageListView.as_view(),
            name='Language_list',
        ),
        path(
            "~create/",
            view=views.LanguageCreateView.as_view(),
            name='Language_create',
        ),
        path("<uuid:pk>/", include([
            path("",
                 view=views.LanguageDetailView.as_view(),
                 name='Language_detail'
                 ),
            path(
                "~update/",
                view=views.LanguageUpdateView.as_view(),
                name='Language_update',
            ),
            path(
                "~delete/",
                view=views.LanguageDeleteView.as_view(),
                name='Language_delete',
            ),
        ])),
    ])),
    path("Family/", include([
        path(
            "",
            view=views.FamilyListView.as_view(),
            name='Family_list',
        ),
        path(
            "~create/",
            view=views.FamilyCreateView.as_view(),
            name='Family_create',
        ),
        path("<uuid:pk>/", include([
            path("",
                 view=views.FamilyDetailView.as_view(),
                 name='Family_detail'
                 ),
            path(
                "~update/",
                view=views.FamilyUpdateView.as_view(),
                name='Family_update',
            ),
            path(
                "~delete/",
                view=views.FamilyDeleteView.as_view(),
                name='Family_delete',
            ),
        ])),
    ])),
    path("Address/", include([
        path(
            "",
            view=views.AddressListView.as_view(),
            name='Address_list',
        ),
        path(
            "~create/",
            view=views.AddressCreateView.as_view(),
            name='Address_create',
        ),
        path("<uuid:pk>/", include([
            path("",
                 view=views.AddressDetailView.as_view(),
                 name='Address_detail'
                 ),
            path(
                "~update/",
                view=views.AddressUpdateView.as_view(),
                name='Address_update',
            ),
            path(
                "~delete/",
                view=views.AddressDeleteView.as_view(),
                name='Address_delete',
            ),
        ])),
    ])),
]
