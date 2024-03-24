from django.http import HttpRequest
from django.shortcuts import render
from .models import MyInfoModel

def intro_view(request: HttpRequest):
    info = MyInfoModel.objects.filter(is_active=True).first()
    context = {"info": info}
    return render(request=request, template_name="includes/intro.html", context=context)


def footer_view(request: HttpRequest):
    info = MyInfoModel.objects.filter(is_active=True).first()
    context = {"info": info}
    return render(request=request, template_name="footer.html", context=context)