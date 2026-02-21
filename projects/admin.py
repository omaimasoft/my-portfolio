from django.contrib import admin

# Register your models here.
# projects/admin.py
from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'link')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)

from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email')
    list_filter = ('sent_at',)


# services/admin.py
from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")


# from django.contrib import admin
# from .models import Profile

# admin.site.register(Profile)


# LES CONTACT POURE MO 
from django.contrib import admin
from .models import Profile, SocialLink

admin.site.register(Profile)
admin.site.register(SocialLink)
