from django.http import HttpRequest
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def consult_popup_view(request: HttpRequest):
    contact_form = ContactForm()
    context = {"form": contact_form}
    return render(request=request, template_name="includes/consulting_popup.html", context=context)