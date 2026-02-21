from django.urls import path
from . import views

app_name = "printed"

urlpatterns = [
    path("", views.printed_list, name="list"),
    path("<slug:slug>/", views.printed_detail, name="detail"),
]
