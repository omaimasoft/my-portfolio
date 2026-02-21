from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Design
from django.utils.html import format_html

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'slug')


@admin.register(Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'design_type', 'published', 'created_at', 'image_tag')
    list_filter = ('design_type', 'category', 'published')
    search_fields = ('title', 'description')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100px;height:auto;object-fit:cover;border-radius:6px;" />', obj.image.url)
        return ""
    image_tag.short_description = 'Preview'
