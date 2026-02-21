from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticPagesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = "https"

    def items(self):
        return [
            "projects:home",
            "projects:contact",
            "projects:services",
            "projects:projects",
            "projects:skills",

            # خليهم غير إلا كانوا موجودين فعلاً ف urls ديالهم:
            "designs:list",
            "printed:list",
        ]

    def location(self, item):
        return reverse(item)