from django import template
from apps.akromdev.models.video_model import VideoLike, Video
from celery import shared_task

register = template.Library()

@shared_task
def check_like(video, user):
    return VideoLike.objects.filter(user = user, video = video).exists()

register.filter(check_like)