# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
    Person,
    Address, Language, Family)


class PersonCreateView(CreateView):
    model = Person


class PersonDeleteView(DeleteView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


class PersonUpdateView(UpdateView):
    model = Person


class PersonListView(ListView):
    model = Person


class FamilyCreateView(CreateView):
    model = Family


class FamilyDeleteView(DeleteView):
    model = Family


class FamilyDetailView(DetailView):
    model = Family


class FamilyUpdateView(UpdateView):
    model = Family


class FamilyListView(ListView):
    model = Family


class LanguageCreateView(CreateView):
    model = Language


class LanguageDeleteView(DeleteView):
    model = Language


class LanguageDetailView(DetailView):
    model = Language


class LanguageUpdateView(UpdateView):
    model = Language


class LanguageListView(ListView):
    model = Language


class AddressCreateView(CreateView):
    model = Address


class AddressDeleteView(DeleteView):
    model = Address


class AddressDetailView(DetailView):
    model = Address


class AddressUpdateView(UpdateView):
    model = Address


class AddressListView(ListView):
    model = Address
