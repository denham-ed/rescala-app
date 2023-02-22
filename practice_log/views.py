from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView


from django.contrib.auth.decorators import login_required

# Create your views here.


# @login_required
class Dashboard(View):
    template_name = "dashboard.html"

    # @login_required
    def get(self, request):
        return render(
            request, 'dashboard.html',
            {"title": "Dashboard"}
        ) 


class Resources(View):

    template_name = "resources.html"


# @login_required
class Log_Practice(View):

    template_name = "log_practice.html"
