from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DeleteView
from django.contrib import messages
from django.urls import reverse

from apps.akromdev.models.video_model import Video, VideoComment, VideoLike
from apps.akromdev.forms.video_form import VideoCommentForm, VideoCreateForm, VideoUpdateForm
from apps.users.models import UserAccount

from apps.akromdev.utils import is_video, is_photo


class VideoView(View):
    def get(self, request):
        videos = Video.objects.all().order_by("-created_at")
        return render(request, "video/videos.html", {
            "videos": videos
        })
    

class VideoDetailView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            video = Video.objects.get(slug = slug)
            videos = Video.objects.filter(category = video.category).order_by("-created_at")
            video_comment = VideoComment.objects.filter(video = video).order_by("-created_at")
            form = VideoCommentForm()

            return render(request, "video/video-detail.html", {
                "title": video.title,
                "video": video,
                "videos": videos,
                "video_comments": video_comment,
                "form": form
            }) 
        return redirect(reverse("users:sign-up"))
    
    def post(self, request, slug):
        if request.user.is_authenticated:
            form = VideoCommentForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data.get("message")
                
                print(message)
                VideoComment.objects.create(
                    user = UserAccount.objects.get(user = request.user), 
                    video = Video.objects.get(slug = slug),
                    message = message)
                
                messages.success(request, "successfully sending comment !")
                return redirect(reverse("akromdev:video-detail", kwargs={"slug": slug}))
            
            messages.error(request, "Your sending message is are not valid !")
            return redirect(reverse("akromdev:video-detail", kwargs={"slug": slug}))

        return redirect(reverse("users:sign-up"))


class VideoCreateView(View):
    def get(self, request):
        form = VideoCreateForm()
        return render(request, "video/video-create.html", {
            "form": form,
        })

    def post(self, request):
        form = VideoCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            cover = cover = form.cleaned_data.get("cover")
            video = video = form.cleaned_data.get("video")

            if is_photo(cover.name):
                if is_video(video.name):
                        Video.objects.create(
                            author = UserAccount.objects.get(user = request.user),
                            title = form.cleaned_data.get("title"),
                            description = form.cleaned_data.get("description"),
                            content = form.cleaned_data.get("content"),
                            category = form.cleaned_data.get("category"),
                            cover = cover,
                            video = video,
                        )
                        messages.success(request, "Successfully create video.")
                        return redirect("akromdev:video-create")

                messages.error(request, "Your video are not valid !")
                return redirect("akromdev:video-create")
            
            messages.error(request, "Your cover are not valid !")
            return redirect("akromdev:video-create")

        messages.error(request, "Your creating fields are not valid !")
        return redirect("akromdev:video-create")
    

class VideoUpdateView(View):
    def get(self, request, slug):
        video = Video.objects.get(slug = slug)
        form = VideoUpdateForm(instance=video)
        return render(request, "video/video-update.html", {
            "form": form,
            "video": video
        })

    def post(self, request, slug):
        video_model = Video.objects.filter(slug = slug)

        form = VideoUpdateForm(
            data=request.POST, 
            instance=video_model.first(),
        )
        if form.is_valid():
            video_model.update(
                author = UserAccount.objects.get(user = request.user),
                title = form.cleaned_data.get("title"),
                description = form.cleaned_data.get("description"),
                category = form.cleaned_data.get("category"),
            )

            messages.success(request, "Successfully updated video")
            return redirect(reverse("akromdev:video-update", kwargs={"slug": video_model.first().slug}))
                
        messages.error(request, "Your fields are not valid !")
        return redirect(reverse("akromdev:video-update", kwargs={"slug": video_model.first().slug}))


class VideoDeleteView(View):
    def get(self, request, slug):
        video = Video.objects.get(slug = slug)
        return render(request, "video/video-delete.html", {
            "video": video
        })
    
    def post(self, request, slug):
        Video.objects.get(slug = slug).delete()
        return redirect("akromdev:videos")
    

def video_like(request, slug):
    if request.user.is_authenticated:
        video = Video.objects.get(slug = slug)

        like, created = VideoLike.objects.get_or_create(
            user=UserAccount.objects.get(user = request.user),
            video=video,
        )
        if not created:
            like.delete()
        return redirect(reverse("akromdev:video-detail", kwargs={"slug": slug}))
    
    return redirect("users:sign-up")