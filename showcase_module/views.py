from django.shortcuts import render
from django.http import HttpRequest
from showcase_module.models import WorkShowCaseModel

# Create your views here.

def workcase_view(request: HttpRequest):
    work_cases = list(WorkShowCaseModel.objects.filter(is_active=True)[:6])
    context = {"work_cases": work_cases}
    return render(request=request, template_name='showcase_module/workshowcase.html', context=context)