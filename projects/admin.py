# projects/admin.py

from django.contrib import admin
from .models import (
    Project,
    Skill,
    ContactMessage,
    Service,
    Profile,
    SocialLink,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "show_on_homepage",
        "homepage_order",
        "created_at",
        "link",
    )

    list_editable = (
        "show_on_homepage",
        "homepage_order",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "show_on_homepage",
        "created_at",
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    search_fields = ("name",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "sent_at")
    search_fields = ("name", "email", "message")
    list_filter = ("sent_at",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "url", "profile")
    search_fields = ("name", "url")
    list_filter = ("icon",)