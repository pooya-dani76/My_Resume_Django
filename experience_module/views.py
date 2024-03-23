from django.shortcuts import render
from django.http import HttpRequest
from experience_module.models import WorkExperienceModel

# Create your views here.

def work_experience_view(request: HttpRequest):
    work_experience = list(WorkExperienceModel.objects.filter(is_active=True).order_by("start_year"))
    context = {"work_experience": work_experience}
    return render(request=request, template_name='experience_module/work_experience.html', context=context)