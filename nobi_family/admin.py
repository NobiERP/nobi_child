# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (Address, Language, Family, Person)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
