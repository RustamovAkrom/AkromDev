from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control rounded-4",
                "id": "floatingInput",
                "placeholder": "Email or Username...",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "class": "form-control rounded-4",
                "id": "floatingPassword",
                "placeholder": "Password...",
            }
        )
    )

__all__ = ("SignUpForm", )