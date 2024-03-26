from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from info_module.models import MyInfoModel
from .forms import ContactForm

#Create your views here.

def consult_popup_view(request: HttpRequest):
    contact_form = ContactForm()
    context = {"form": contact_form}
    return render(request=request, template_name="includes/consulting_popup.html", context=context)

class ContactUsView(View):
    def get(self, request: HttpRequest):
        contact_form = ContactForm()
        info = MyInfoModel.objects.filter(is_active=True).first()
        context = {"form": contact_form, "info":info}
        return render(request=request, template_name="contact/contact.html", context=context)
    
    def post(self, request: HttpRequest):
        print("Hello From Contact Us")
        contact_form: ContactForm = ContactForm(request.POST or None)
        if contact_form.is_valid():
            contact_form.save()
        return redirect(reverse('contact-us'))  
