from django import forms

from .models import User, UserAccount


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class SignIn(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "password_change")


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ("avatar", "bio", "bg_account_image", "birthday", "phone_number", "gender", "country", "socials")