import profile

from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
from community.models import Profile, Category, Contact


class RegistrationForm(SignupForm):
    class Meta():
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['Email'].label = "Email Address"


class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile

        fields = ['picture', 'id']

        labels = {'picture': ''}


class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = "__all__"
