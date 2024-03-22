from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .models import MyInfo, Services
from utils.services import divideList


class HomeView(View):
    def post(self, request: HttpRequest):
        pass

    def get(self, request: HttpRequest):
        info = MyInfo.objects.filter(is_active=True).first()
        services = divideList(obj_list=list(Services.objects.all()), division_to=4)
        context = {
            "info": info,
            "services": services,
        }
        return render(request=request, template_name='info_module/index-2.html', context=context)