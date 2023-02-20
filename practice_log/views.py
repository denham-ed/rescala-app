from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.


class Dashboard(TemplateView):
    template_name = "dashboard.html"


class Resources(TemplateView):

    template_name = "resources.html"


class Log_Practice(TemplateView):

    template_name = "resources.html"