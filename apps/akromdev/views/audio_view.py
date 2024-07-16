from django.views.generic import TemplateView


class AudioView(TemplateView):
    template_name = "audio/audios.html"