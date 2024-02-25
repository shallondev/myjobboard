from django.forms import ModelForm
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import JobListing


class CreateListingForm(ModelForm):
    class Meta:
        model = JobListing
        fields = [
            'position_title', 'company', 'city', 'province_state', 'country', 'logo_url', 'employment_type', 'is_remote', 
            'summary', 'responsibilities', 'must_have', 'qualifications', 'bonus_skills', 'annual_salary',
            ]
        widgets = {
            'position_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'province_state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Province/State'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'logo_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Image URL of company logo'}),
            'employment_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E.g. Full-time, Par-time, Contract...'}),
            'summary': forms.CharField(widget=CKEditorWidget()),
            'responsibilities': forms.CharField(widget=CKEditorWidget()),
            'must_have': forms.CharField(widget=CKEditorWidget()),
            'qualifications': forms.CharField(widget=CKEditorWidget()),
            'bonus_skills': forms.CharField(widget=CKEditorWidget()),
            'annual_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter expected annual salary'}),
        }
        required = {
            'position_title': True,
            'company': True,
            'country': True,
            'image_url': False,
            'summary' : True,
            'is_remote' : True,
        }