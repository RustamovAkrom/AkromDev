from django.urls import path
from .views import IndexView, ContactView, AboutView, VideoView,VideoDetailView, PictureView, PictureDetailView, AudioView


app_name = "akromdev"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("pictures/", PictureView.as_view(), name="pictures"),
    path("picture-detail/<str:slug>", PictureDetailView.as_view(), name="picture-detail"),
    path("videos/", VideoView.as_view(), name="videos"),
    path("audios/", AudioView.as_view(), name="audios"),
    path("video-detail/<str:slug>", VideoDetailView.as_view(), name="video-detail")
]