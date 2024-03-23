from django.shortcuts import render
from django.http import HttpRequest
from services_module.models import ServicesModel
from utils.services import divideList

# Create your views here.

def services_view(request: HttpRequest):
    services = divideList(obj_list=list(
        ServicesModel.objects.filter(is_active=True)), division_to=4)
    context = {'services': services}
    return render(request=request, template_name="services_module/services.html", context=context)