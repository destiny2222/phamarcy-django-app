from django import forms
from .models import  Tutor
from django.template.defaultfilters import slugify
#...



class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = '__all__'