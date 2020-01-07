from django import forms

from .models import Family


class FamilyCreationForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ('name', 'owner', 'members')


class FamilyChangeForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ('name', 'owner', 'members')
