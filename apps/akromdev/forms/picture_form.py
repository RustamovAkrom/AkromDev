from django import forms
from apps.akromdev.models.picture_model import Picture


class PictureCreateForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "type": "file", "name": "image", "class": "form-control"
    }))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "type": "text", "name": "description", "class": "form-control"
    }))


class PictureUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={
        "type": "file", "name": "image", "class": "form-control"
    }))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "type": "text", "name": "description", "class": "form-control"
    }))

    class Meta:
        model = Picture
        fields = ("image", "description")