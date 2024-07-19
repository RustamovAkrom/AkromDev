from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
from apps.akromdev.models.picture_model import Picture


class PictureView(TemplateView):
    template_name = "picture/pictures.html"


class PictureDetailView(View):
    def get(self, request, slug):
        picture = Picture.objects.get(slug = slug)
        return render(request, "picture/picture-detail.html", {
            "picture": picture
        })