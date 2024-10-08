from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from django.urls import reverse

from apps.akromdev.models.video_model import (
    Video,
    VideoComment,
    VideoLike,
    VideoCategory,
)
from apps.akromdev.forms.video_form import (
    VideoCommentForm,
    VideoCreateForm,
    VideoUpdateForm,
)
from apps.users.models import UserAccount
from apps.akromdev.utils import is_video, is_photo

import markdown2


class VideoView(View):
    def get(self, request):
        category_filter_name = request.GET.get("category", None)
        search_filter_name = request.GET.get("search", None)

        if search_filter_name is not None:
            videos = Video.objects.filter(title__icontains=search_filter_name).order_by(
                "-created_at"
            )

            if not videos:
                videos = Video.objects.filter(
                    category=VideoCategory.objects.filter(
                        name__icontains=search_filter_name
                    ).first()
                ).order_by("-created_at")

        else:
            if category_filter_name is not None:
                videos = Video.objects.select_related("category").filter(
                    category=get_object_or_404(VideoCategory, name=category_filter_name)
                ).order_by("-created_at")
            else:
                videos = Video.objects.select_related("category").all().order_by("-created_at")

        categories = VideoCategory.objects.all()

        return render(
            request, "video/videos.html", {"videos": videos, "categories": categories}
        )


class VideoDetailView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            video = get_object_or_404(Video, slug=slug)
            videos = Video.objects.filter(category=video.category).order_by(
                "-created_at"
            )
            video_comment = VideoComment.objects.filter(video=video).order_by(
                "-created_at"
            )
            form = VideoCommentForm()

            return render(
                request,
                "video/video-detail.html",
                {
                    "title": video.title,
                    "video_content_html": markdown2.markdown(video.content),
                    "video": video,
                    "videos": videos,
                    "video_comments": video_comment,
                    "form": form,
                },
            )
        return redirect(reverse("users:sign-up"))

    def post(self, request, slug):
        if request.user.is_authenticated:
            form = VideoCommentForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data.get("message")

                print(message)
                VideoComment.objects.create(
                    user=get_object_or_404(UserAccount, user=request.user),
                    video=get_object_or_404(Video, slug=slug),
                    message=message,
                )

                messages.success(request, "successfully sending comment !")
                return redirect(reverse("akromdev:video-detail", kwargs={"slug": slug}))

            messages.error(request, "Your sending message is are not valid !")
            return redirect(reverse("akromdev:video-detail", kwargs={"slug": slug}))

        return redirect(reverse("users:sign-up"))


class VideoCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = VideoCreateForm()
        return render(
            request,
            "video/video-create.html",
            {
                "form": form,
            },
        )

    def post(self, request):
        form = VideoCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            cover = cover = form.cleaned_data.get("cover")
            video = video = form.cleaned_data.get("video")

            if is_photo(cover.name):
                if is_video(video.name):
                    Video.objects.create(
                        author=get_object_or_404(UserAccount, user=request.user),
                        title=form.cleaned_data.get("title"),
                        description=form.cleaned_data.get("description"),
                        content=form.cleaned_data.get("content"),
                        category=form.cleaned_data.get("category"),
                        cover=cover,
                        video=video,
                    )
                    messages.success(request, "Successfully create video.")
                    return redirect("akromdev:video-create")

                messages.error(request, "Your video are not valid !")
                return redirect("akromdev:video-create")

            messages.error(request, "Your cover are not valid !")
            return redirect("akromdev:video-create")

        messages.error(request, "Your creating fields are not valid !")
        return redirect("akromdev:video-create")


class VideoUpdateView(LoginRequiredMixin, View):
    def get(self, request, slug):
        video = get_object_or_404(Video, slug=slug)
        form = VideoUpdateForm(instance=video)
        return render(
            request, "video/video-update.html", {"form": form, "video": video}
        )

    def post(self, request, slug):
        video_model = Video.objects.filter(slug=slug)

        form = VideoUpdateForm(
            data=request.POST,
            instance=video_model.first(),
        )
        if form.is_valid():
            video_model.update(
                author=get_object_or_404(UserAccount, user=request.user),
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                category=form.cleaned_data.get("category"),
            )

            messages.success(request, "Successfully updated video")
            return redirect(
                reverse(
                    "akromdev:video-update", kwargs={"slug": video_model.first().slug}
                )
            )

        messages.error(request, "Your fields are not valid !")
        return redirect(
            reverse("akromdev:video-update", kwargs={"slug": video_model.first().slug})
        )


class VideoDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug):
        video = get_object_or_404(Video, slug=slug)
        return render(request, "video/video-delete.html", {"video": video})

    def post(self, request, slug):
        get_object_or_404(Video, slug=slug).delete()
        return redirect("akromdev:videos")


@login_required
def video_like(request, slug):
    if request.user.is_authenticated:
        video = get_object_or_404(Video, slug=slug)

        like, created = VideoLike.objects.get_or_create(
            user=get_object_or_404(UserAccount, user=request.user),
            video=video,
        )
        if not created:
            like.delete()
        return redirect(reverse("akromdev:video-detail", kwargs={"slug": slug}))

    return redirect("users:sign-up")
