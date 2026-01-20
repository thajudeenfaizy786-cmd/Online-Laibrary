from django import forms
from.models import Collections,Profile
from django.contrib.auth.models import User
class BookForm(forms.ModelForm):
    class Meta:
        model= Collections
        fields= "__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']       