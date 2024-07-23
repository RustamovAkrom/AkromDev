from typing import Any
from django import forms
from apps.akromdev.models.video_model import VideoComment, Video, VideoCategory


class VideoCommentForm(forms.Form):
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control me-2",
                "placeholder": "Send message...",
                "area-label": "Send",
            }
        )
    )


class VideoCreateForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "title",
                "class": "form-control",
                "placeholder": "title...",
            }
        ),
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "description",
                "class": "form-control",
                "placeholder": "description...",
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "content",
                "class": "form-control",
                "placeholder": "content...",
            }
        )
    )
    cover = forms.ImageField(
        widget=forms.FileInput(
            attrs={"type": "file", "name": "cover", "class": "form-control"}
        )
    )
    video = forms.FileField(
        widget=forms.FileInput(
            attrs={"type": "file", "name": "video", "class": "form-control"}
        )
    )

    class Meta:
        model = Video
        fields = (
            "title",
            "description",
            "content",
            "category",
            "cover",
            "video",
        )


class VideoUpdateForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "title",
                "class": "form-control",
                "placeholder": "title...",
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "description",
                "class": "form-control",
                "placeholder": "description...",
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "content",
                "class": "form-control",
                "placeholder": "content...",
            }
        )
    )

    class Meta:
        model = Video
        fields = (
            "title",
            "description",
            "content",
            "category",
        )
