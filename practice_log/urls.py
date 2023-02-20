from . import views
from django.urls import path

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('resources', views.Resources().as_view(), name='resources'),
    path('log', views.Resources().as_view(), name='log_a_practice'),
]