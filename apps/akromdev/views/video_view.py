from django.views.generic import TemplateView


class VideoView(TemplateView):
    template_name = "video/videos.html"