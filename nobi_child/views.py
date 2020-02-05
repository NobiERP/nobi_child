# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Child,
)


class ChildCreateView(CreateView):

    model = Child


class ChildDeleteView(DeleteView):

    model = Child


class ChildDetailView(DetailView):

    model = Child


class ChildUpdateView(UpdateView):

    model = Child


class ChildListView(ListView):

    model = Child

