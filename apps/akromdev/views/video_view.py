from django.shortcuts import render, redirect, get_list_or_404
from django.views import View

from apps.akromdev.models.video_model import Video


class VideoView(View):
    def get(self, request):
        videos = Video.objects.all().order_by("-created_at")
        return render(request, "video/videos.html", {
            "videos": videos
        })
    

class VideoDetailView(View):
    def get(self, request, slug):
        videos = Video.objects.all()
        video = Video.objects.get(slug = slug)
        print(video)
        return render(request, "video/video_detail.html", {
            "video": video,
            "videos": videos,
            "video_comments": None
        }) 