from django import forms
from apps.akromdev.models.contact_model import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "your name...",
            }
        )
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "your subject...",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "your email",
            }
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "message",
                "id": "message",
                "class": "form-control",
                "placeholder": "message...",
            }
        )
    )

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")
