from django.shortcuts import render
from allauth.account.views import SignupView


class CustomSignUpView(SignupView):
    template_name = "templates/account/signup.html"

