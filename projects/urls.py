from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.home, name="home"),         
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path("projects/", views.projects, name="projects"),
    path("skills/", views.skills, name="skills"),
]