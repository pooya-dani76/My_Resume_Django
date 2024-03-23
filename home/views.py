from django.shortcuts import render
from django.views import View
from django.http import HttpRequest

# Create your views here.

def header_menu_view(request: HttpRequest):
    return render(request=request, template_name="includes/header_menu.html")


class HomeView(View):
    def post(self, request: HttpRequest):
        pass

    def get(self, request: HttpRequest):
        context = {}
        return render(request=request, template_name='home/index-2.html', context=context)