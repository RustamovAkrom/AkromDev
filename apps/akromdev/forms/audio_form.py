from django import forms
from apps.akromdev.models.audio_model import Audio


class AudioCreateForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"type": "text", "name": "title", "class": "form-control"}
        ),
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "description",
                "name": "description",
                "class": "form-control",
            }
        )
    )
    cover = forms.ImageField(
        widget=forms.FileInput(
            attrs={"type": "file", "name": "cover", "class": "form-control"}
        )
    )
    audio = forms.FileField(
        widget=forms.FileInput(
            attrs={"type": "file", "name": "audio", "class": "form-control"}
        )
    )

    class Meta:
        model = Audio
        fields = ("title", "description", "cover", "audio", "category")


class AudioUpdateForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"type": "text", "name": "title", "class": "form-control"}
        ),
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "description",
                "name": "description",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Audio
        fields = ("title", "description", "category")
