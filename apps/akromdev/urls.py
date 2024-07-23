from django.urls import path
from .views.home_view import IndexView
from .views.contact_view import ContactView
from .views.video_view import (
    VideoView,
    VideoDetailView,
    VideoCreateView,
    VideoDeleteView,
    VideoUpdateView,
    video_like,
)
from .views.about_view import AboutView
from .views.picture_view import (
    PictureView,
    PictureDetailView,
    PictureCreateView,
    PictureDeleteView,
    PictureUpdateView,
)
from .views.audio_view import AudioView, AudioDetailView, AudioCreateView, AudioUpdateView, AudioDeleteView


app_name = "akromdev"

urlpatterns = [
    path("", IndexView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("pictures/", PictureView.as_view(), name="pictures"),
    path("picture-create/", PictureCreateView.as_view(), name="picture-create"),
    path(
        "picture-detail/<str:slug>", PictureDetailView.as_view(), name="picture-detail"
    ),
    path(
        "picture-update/<str:slug>", PictureUpdateView.as_view(), name="picture-update"
    ),
    path(
        "picture-delete/<str:slug>", PictureDeleteView.as_view(), name="picture-delete"
    ),
    path("videos/", VideoView.as_view(), name="videos"),
    path("video-create/", VideoCreateView.as_view(), name="video-create"),
    path("video-detail/<str:slug>", VideoDetailView.as_view(), name="video-detail"),
    path("video-update/<str:slug>", VideoUpdateView.as_view(), name="video-update"),
    path("video-delete/<str:slug>", VideoDeleteView.as_view(), name="video-delete"),
    path("video-like/<str:slug>", video_like, name="video-like"),
    path("audios/", AudioView.as_view(), name="audios"),
    path("audio-create/", AudioCreateView.as_view(), name="audio-create"),
    path("audio-detail/<str:slug>", AudioDetailView.as_view(), name="audio-detail"),
    path("audio-update/<str:slug>", AudioUpdateView.as_view(), name="audio-update"),
    path("audio-delete/<str:slug>", AudioDeleteView.as_view(), name="audio-delete")
]
