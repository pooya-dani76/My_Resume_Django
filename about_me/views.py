from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from experience_module.models import WorkExperienceModel

from .models import AbilitiesModel, EducationModel
from info_module.models import MyInfoModel

# Create your views here.


class AboutMeView(View):
    def get(self, request: HttpRequest):
        info = MyInfoModel.objects.filter(is_active=True).first()
        abilities = list(AbilitiesModel.objects.filter(is_active=True))
        experiences = list(WorkExperienceModel.objects.filter(
            is_active=True).order_by("-start_year"))
        educations = list(EducationModel.objects.filter(
            is_active=True).order_by("-start_year"))
        context = {"info": info, "abilities": abilities,
                   "experiences": experiences, "educations": educations}
        return render(request=request, template_name='about_me/about.html', context=context)

    def post(self, request: HttpRequest):
        pass
