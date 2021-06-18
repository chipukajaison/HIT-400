from django.forms import ModelForm, DecimalField
from .models import Patient
from django import forms

class NewPatientrecord(ModelForm):
    pregnancies = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    glucose = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    blood_pressure = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    skin_thickness = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    insulin = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    BMI = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    diabetes_pedigree_function = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.DecimalField(max_digits=400, decimal_places=4, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = ['pregnancies', 'glucose', 'blood_pressure', 'skin_thickness', 'insulin', 'BMI', 'diabetes_pedigree_function','age']