from django import forms
from apps.akromdev.models.blog_model import Post


class PostUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "title",
                "class": "form-control",
                "placeholder": "Title",
            }
        )
    )
    bg_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "type": "file",
                "name": "bg_image",
                "class": "form-control",
                "placeholder": "Baground image",
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
                "placeholder": "Description",
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"name": "content", "class": "form-control", "placeholder": "Content"}
        )
    )
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"type": "checkbox", "name": "is_active"})
    )

    class Meta:
        model = Post
        fields = ("title", "bg_image", "description", "content", "is_active")


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "name": "title",
                "class": "form-control",
                "placeholder": "Title",
            }
        )
    )
    bg_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "type": "file",
                "name": "bg_image",
                "class": "form-control",
                "placeholder": "Baground image",
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
                "placeholder": "Description",
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={"name": "content", "class": "form-control", "placeholder": "Content"}
        )
    )
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"type": "checkbox", "name": "is_active"})
    )

    class Meta:
        model = Post
        fields = ("title", "bg_image", "description", "content", "is_active")
