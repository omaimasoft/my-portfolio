from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Design

class DesignsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.85
    protocol = "https"

    def items(self):
        return Design.objects.all()

    def lastmod(self, obj):
        return getattr(obj, "updated_at", None) or getattr(obj, "created_at", None)

    def location(self, obj):
        # إذا ما عندكش slug استعملي id/pk
        return reverse("designs:detail", args=[obj.pk])