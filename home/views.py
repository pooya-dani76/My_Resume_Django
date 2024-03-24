from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.http import HttpRequest
from popup.forms import ContactForm

# Create your views here.

def header_menu_view(request: HttpRequest):
    return render(request=request, template_name="includes/header_menu.html")


class HomeView(View):
    def post(self, request: HttpRequest):
        contact_form: ContactForm = ContactForm(request.POST or None)
        if contact_form.is_valid():
            contact_form.save()
        return redirect(reverse('home'))    

    def get(self, request: HttpRequest):
        context = {}
        return render(request=request, template_name='home/index-2.html', context=context)