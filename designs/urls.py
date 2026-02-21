from django.urls import path
from . import views

app_name = 'designs'

urlpatterns = [
    path('', views.designs_list, name='list'),
    path('<int:pk>/', views.design_detail, name='detail'),
]
