from django.views.generic import TemplateView


class PictureView(TemplateView):
    template_name = "picture/pictures.html"