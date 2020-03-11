# -*- coding: utf-8 -*-
import os
import uuid

from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField

from model_utils.models import TimeStampedModel, StatusModel
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

from nobi_family.utils import get_unique_slug


class Address(TimeStampedModel):
    """
    Models to store the address from person
    """
    number = models.CharField(_("Number"), max_length=15)
    street = models.CharField(_("Street"), max_length=255)
    zip = models.PositiveIntegerField(_("ZIP"))
    city = models.CharField(_("City"), max_length=255)
    department = models.CharField(_("Department"), max_length=255)
    country = models.CharField(_("Country"), max_length=100)

    class Meta:
        ordering = ('country', 'department', 'zip', 'city', 'street', 'number')
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return "{}, {}, {} {} ({})".format(self.number, self.street, self.zip, self.city, self.country)


class Language(TimeStampedModel):
    """
    Models to store language
    """
    name = models.CharField(_("Name"), max_length=100, unique=True)

    class Meta:
        ordering = ("name", "created",)
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")

    def __str__(self):
        # return name of language
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # set slug, title field
        self.name = self.name.title()
        return super(Language, self).save()


class Family(models.Model):
    """
    Model for Family
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=255)
    persons = models.ManyToManyField(
        "Person",
        related_name="family_person",
    )

    class Meta:
        # ordering = ('', '',)
        verbose_name = _('Family')
        verbose_name_plural = _("Families")

    def __str__(self):
        return self.name


class Person(StatusModel, models.Model):
    """
    General model for a person
    """
    STATUS = Choices(
        ("in_progress", _("In progress")),
        ("archived", _("Archived")),
    )
    GENDER_CHOICES = Choices(
        ("man", _("Man")),
        ("woman", _("Woman")),
        ("boy", _("Boy")),
        ("girl", _("Girl")),
        ("other", _("Other")),
        ("unknown", _("Unknown")),
    )
    def upload_picture(self, filename):
        f, ext = os.path.splitext(filename)
        upload_to = "person/%s/" % self.slug
        return '%s%s%s' % (upload_to, uuid.uuid4().hex, ext)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    alive = models.BooleanField(_("Alive"), default=True)
    email = models.EmailField(_("Email"), blank=True, null=True, )
    phone = PhoneNumberField(verbose_name=_("Phone"), blank=True, null=True, )
    mobile_phone = PhoneNumberField(verbose_name=_("Mobile phone"), blank=True, null=True)
    professional_phone = PhoneNumberField(verbose_name=_("Professional phone"), blank=True, null=True)
    slug = models.SlugField(_("Slug"))
    picture = models.ImageField(_("Picture"), upload_to=upload_picture, blank=True, null=True)
    birth_date = models.DateField(_("Birth date"), blank=True, null=True)

    couple = models.ForeignKey(
        to="self",
        verbose_name=_("Couple"),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    parents = models.ManyToManyField(
        to="self",
        verbose_name=_("Parents"),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    children = models.ManyToManyField(
        to="self",
        verbose_name=_("Children"),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    fraternities = models.ManyToManyField(
        to="self",
        verbose_name=_("Fraternities"),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    languages = models.ManyToManyField(
        to="Language",
        verbose_name=_("Languages"),
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
    )
    address = models.ForeignKey(
        to="Address",
        verbose_name=_("Address"),
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
        blank=True,
        null=True,
    )
    gender = StatusField(_("Gender"), choices_name="GENDER_CHOICES", blank=False, null=True)


    class Meta:
        ordering = ('first_name', 'last_name',)
        verbose_name = _('Person')
        # verbose_name_plural = _('Persons')

    def __str__(self):
        return "{}".format(self.full_name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # set slug, title field
        self.slug = get_unique_slug(self, 'full_name', 'slug')
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        return super(Person, self).save()

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    full_name.fget.short_description = _("Full name")

