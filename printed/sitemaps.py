from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import PrintedProduct

class PrintedProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = "https"

    def items(self):
        return PrintedProduct.objects.all()

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None) or getattr(obj, "created_at", None)

    def location(self, obj):
        # خاص route name تكون صحيحة ف printed/urls.py
        # مثال: path("<slug:slug>/", views.detail, name="detail")
        return reverse("printed:detail", args=[obj.slug])