from typing import Any
from django import forms
from django.core.exceptions import ValidationError
import phonenumber_field.modelfields

from .models import User, UserAccount

from phonenumber_field.formfields import PhoneNumberField


class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control rounded-4", "id": "floatingInput", "placeholder": "Email or Username..."
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type": "password", "class": "form-control rounded-4", "id": "floatingPassword", "placeholder": "Password..."
    }))


class SignInForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control rounded-4", "placeholder": "First name..."
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control rounded-4", "placeholder": "Last name..."
    }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control rounded-4", "placeholder": "Username..."
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "type": "email", "class": "form-control rounded-4", "placeholder": "Email..."
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "type": "password", "class": "form-control rounded-4", "placeholder": "Password..."
    }))
    password_change = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "type": "password", "class": "form-control rounded-4", "placeholder": "Password (Change)..."
    }))

    def save(self, commit=True) -> Any:
        user = super().save(commit)
        password = self.cleaned_data.get("password")
        password_change = self.cleaned_data.get("password_change")

        if password == password_change:
            user.set_password(password)
            user.save()
            UserAccount.objects.create(
                user = user,
                first_name = user.first_name,
                last_name = user.last_name,
                username = user.username,
                email = user.email
            )
            
        else:
            raise ValidationError("password and password_change must be match")

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password", "password_change")


class UserAccountForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "firstName", "placeholder": ""
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "lastName", "placeholder": ""
    }))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "username", "placeholder": ""
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        "type": "email", "class": "form-control", "id": "email", "placeholder": "you@example.com"
    }))
    avatar = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        "type": "file", "class": "form-control", "id": "username", "placeholder": ""
    }))
    bio = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "bio", "placeholder": ""
    }))
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={
        "type": "date", "class": "form-control", "id": "birthday", "placeholder": ""
    }))
    phone_number = PhoneNumberField(required=False, widget=forms.TextInput(attrs={
        "type": "tel", "class": "form-control", "id": "phone_number", "placeholder": ""
    }), region="UZ")
    gender = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    country = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "type": "text", "class": "form-control", "id": "country", "placeholder": ""
    })) 
    socials = forms.CharField(required=False, widget=forms.TextInput())
    
    class Meta:
        model = UserAccount
        fields = ("first_name", "last_name", "username", "email", "avatar", "bio", "birthday", "phone_number", "gender", "country", "socials")


