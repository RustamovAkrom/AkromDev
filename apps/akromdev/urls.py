from django.urls import path
from .views.home_view import IndexView
from .views.contact_view import ContactView
from .views.about_view import AboutView

from .views.video_view import (
    VideoView,
    VideoDetailView,
    VideoCreateView,
    VideoDeleteView,
    VideoUpdateView,
    video_like,
)
from .views.picture_view import (
    PictureView,
    PictureDetailView,
    PictureCreateView,
    PictureDeleteView,
    PictureUpdateView,
)
from .views.audio_view import (
    AudioView, 
    AudioDetailView, 
    AudioCreateView, 
    AudioUpdateView, 
    AudioDeleteView
)
from .views.blog_view import (
    BlogPostDetail,
    BlogPostView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView,
)


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
    path("blog-posts/", BlogPostView.as_view(), name="posts"),
    path("blog-post-detail/<str:slug>", BlogPostDetail.as_view(), name="post-detail"),
    path("post-update/<str:slug>", PostUpdateView.as_view(), name="post-update"),
    path("post-delete/<str:slug>", PostDeleteView.as_view(), name="post-delete"),
    path("post-create/", PostCreateView.as_view(), name="post-create"),
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
