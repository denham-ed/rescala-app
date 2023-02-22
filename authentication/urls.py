from django.urls import path, include
from . import views

urlpatterns = [
    path(
        'accounts/signup/',
        views.CustomSignUpView.as_view(),
        name='custom_signup')
]