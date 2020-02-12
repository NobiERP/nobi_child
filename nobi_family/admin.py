# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
   Child,
)


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    pass



