import os
from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from .models import MyInfoModel

def intro_view(request: HttpRequest):
    info = MyInfoModel.objects.filter(is_active=True).first()
    print(info.resume_file.path)
    print(info.resume_file.url)
    context = {"info": info}
    return render(request=request, template_name="includes/intro.html", context=context)


def footer_view(request: HttpRequest):
    info = MyInfoModel.objects.filter(is_active=True).first()
    context = {"info": info}
    return render(request=request, template_name="footer.html", context=context)


def download_resume(request):
    info = MyInfoModel.objects.filter(is_active=True).first()
    file_path = os.path.join(settings.MEDIA_ROOT, info.resume_file.path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404