from django import forms
from django.core.exceptions import ValidationError
from apps.users.models.useraccount_model import UserAccount
from apps.users.models.user_model import User


class SignInForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "placeholder": "First name...",
            }
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "placeholder": "Last name...",
            }
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "placeholder": "Username...",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control rounded-4",
                "placeholder": "Email...",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control rounded-4",
                "placeholder": "Password...",
            }
        ),
    )
    password_change = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control rounded-4",
                "placeholder": "Password (Change)...",
            }
        ),
    )

    def save(self, commit=True):
        user = super().save(commit)
        password = self.cleaned_data.get("password")
        password_change = self.cleaned_data.get("password_change")

        if password == password_change:
            user.set_password(password)
            user.save()
            UserAccount.objects.create(
                user=user,
                first_name=user.first_name,
                last_name=user.last_name,
                username=user.username,
                email=user.email,
            )

        else:
            raise ValidationError("password and password_change must be match")

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password_change",
        )


__all__ = ("SignInForm",)
