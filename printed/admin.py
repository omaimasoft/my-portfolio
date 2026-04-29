from django.contrib import admin
from .models import PrintedCategory, PrintedProduct, PrintedProductImage


class PrintedProductImageInline(admin.TabularInline):
    model = PrintedProductImage
    extra = 1


@admin.register(PrintedCategory)
class PrintedCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(PrintedProduct)
class PrintedProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "is_available", "is_featured", "created_at")
    list_filter = ("category", "is_available", "is_featured", "created_at")
    search_fields = ("title", "description", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PrintedProductImageInline]

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "category",
                "title",
                "slug",
                "price",
                "main_image",
                "video",
            )
        }),
        ("Descriptions", {
            "fields": (
                "short_description",
                "description",
            )
        }),
        ("Product Details", {
            "fields": (
                "capacity",
                "material",
                "lid",
                "straw",
                "design",
                "use",
                "care",
            )
        }),
        ("Availability", {
            "fields": (
                "is_available",
                "delivery_info",
                "is_featured",
            )
        }),
    )


admin.site.register(PrintedProductImage)