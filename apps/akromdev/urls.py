from django.urls import path
from .views import IndexView, ContactView, AboutView, VideoView, PictureView, AudioView


app_name = "akromdev"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("pictures/", PictureView.as_view(), name="pictures"),
    path("videos/", VideoView.as_view(), name="videos"),
    path("audios/", AudioView.as_view(), name="audios"),
]