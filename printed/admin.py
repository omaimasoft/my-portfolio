from django.contrib import admin
from .models import (
    PrintedCategory,
    PrintedProduct,
    PrintedProductImage
)

# ================== INLINE IMAGES ==================

class PrintedProductImageInline(admin.TabularInline):
    model = PrintedProductImage
    extra = 2


# ================== PRODUCT ADMIN ==================

@admin.register(PrintedProduct)
class PrintedProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'price',
        'is_featured',
        'created_at',
    )

    list_filter = (
        'category',
        'is_featured',
    )

    search_fields = (
        'title',
        'description',
    )

    list_editable = (
        'is_featured',
    )

    inlines = [PrintedProductImageInline]

    readonly_fields = (
        'created_at',
    )


# ================== CATEGORY ADMIN ==================

@admin.register(PrintedCategory)
class PrintedCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {
        'slug': ('name',)
    }
