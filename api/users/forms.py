from django import forms
from django.contrib.auth.forms import UserCreationForm as CreationForm, UserChangeForm as ChangeForm
from .models import User


class UserCreationForm(CreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserChangeForm(ChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
