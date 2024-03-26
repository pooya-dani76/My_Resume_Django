from django import forms
from .models import ConsultModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ConsultModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"placeholder" : "Your Name *"}),
            'email': forms.TextInput(attrs={"placeholder":"Your Email *"}),
            'message': forms.Textarea(attrs={"placeholder":"Your Message *"}),
        }
        error_messages = {
            'name': {
                'required': 'Your Name is Required'
            },
            'email': {
                'required': 'Your Email is Required'
            },
            'message': {
                'required': 'Message is Required'
            },
        }