from django.contrib.auth.models import User
from third_app.models import userinfo
from django import forms

class Userinfoform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
class userinfoform(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ['portfolio', 'profile_pic']