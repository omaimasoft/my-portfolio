from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import index, sitemap
from django.views.generic import TemplateView

# Sitemap classes
from projects.sitemaps import StaticPagesSitemap
from printed.sitemaps import PrintedProductSitemap
from designs.sitemaps import DesignsSitemap  # إذا مازال ماوجدتيهش علّقيه مؤقتًا

sitemaps = {
    "static": StaticPagesSitemap,
    "printed": PrintedProductSitemap,
    "designs": DesignsSitemap,  # علّقيه إذا مازال ماوجدتيهش
}

urlpatterns = [
    path("admin/", admin.site.urls),

    # Sitemap index (الرئيسي)
    path(
        "sitemap.xml",
        index,
        {"sitemaps": sitemaps, "sitemap_url_name": "sitemaps"},
        name="django.contrib.sitemaps.views.index",
    ),

    # Sitemap sections (مقسمة)
    path(
        "sitemap-<section>.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemaps",
    ),

    # robots.txt
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),

    # Apps
    path("", include(("projects.urls", "projects"), namespace="projects")),
    path("designs/", include(("designs.urls", "designs"), namespace="designs")),
    path("printed/", include(("printed.urls", "printed"), namespace="printed")),
]

# Media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)