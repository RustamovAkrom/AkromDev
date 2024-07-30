from django import forms
from phonenumber_field.formfields import PhoneNumberField
from apps.users.models.useraccount_model import UserAccount


class UserAccountForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "firstName",
                "placeholder": "",
            }
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "lastName",
                "placeholder": "",
            }
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "username",
                "placeholder": "",
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "id": "email",
                "placeholder": "you@example.com",
            }
        ),
    )
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "type": "file",
                "class": "form-control",
                "id": "username",
                "placeholder": "",
            }
        ),
    )
    bio = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "bio",
                "placeholder": "",
            }
        ),
    )
    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "id": "birthday",
                "placeholder": "",
            }
        ),
    )
    phone_number = PhoneNumberField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "class": "form-control",
                "id": "phone_number",
                "placeholder": "",
            }
        ),
        region="UZ",
    )
    # gender = forms.CharField(required=False, widget=forms.TextInput(attrs={
    #     "class": "form-control"
    # }))
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "country",
                "placeholder": "",
            }
        ),
    )
    socials = forms.CharField(required=False, widget=forms.TextInput())

    class Meta:
        model = UserAccount
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "avatar",
            "bio",
            "birthday",
            "phone_number",
            "gender",
            "country",
            "socials",
        )


__all__ = ("UserAccountForm",)
