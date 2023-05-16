from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'misId', 'email', 'year', 'division', 'department', 'cgpa', 'attendance']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'misId': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'division': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'cgpa': forms.TextInput(attrs={'class': 'form-control'}),
            'attendance': forms.TextInput(attrs={'class': 'form-control'}),
        }