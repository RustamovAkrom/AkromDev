from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.users.models import User, UserAccount
from apps.akromdev.models import Video, Picture, Audio


class UserProfileView(View):
    def get(self, request, username):
        if request.user.is_authenticated:
            if username[0] == "@":

                user = User.objects.get(username=username[1:])
                user_account = get_object_or_404(UserAccount, user=user)
                videos = Video.objects.filter(author=user_account).order_by(
                    "-created_at"
                )
                audios = Audio.objects.filter(author=user_account).order_by(
                    "created_at"
                )
                pictures = Picture.objects.filter(author=user_account).order_by(
                    "-created_at"
                )

                return render(
                    request,
                    "user/user_profile.html",
                    {
                        "user_account": user_account,
                        "videos": videos,
                        "audios": audios,
                        "pictures": pictures,
                    },
                )

            messages.error(request, "Now validate username not found '@' ")
            return redirect("akromdev:videos")

        return redirect("users:sign-up")

__all__ = ("UserProfileView", )