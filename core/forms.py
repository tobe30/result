# dashboard/forms.py
from django import forms
from .models import  Semester, Session


class CheckResult(forms.Form):
    session = forms.ModelChoiceField(
    queryset=Session.objects.all(),
    empty_label="Select a session",
    required=True,
    widget=forms.Select(attrs={'class': 'form-select'})
)

    semester = forms.ModelChoiceField(
    queryset=Semester.objects.all(), 
    empty_label="Select a Semester",
    required=True,  
    widget=forms.Select(attrs={'class': 'form-select'}))
