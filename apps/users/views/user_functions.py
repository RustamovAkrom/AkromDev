from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from apps.users.models.useraccount_model import UserAccount


@login_required
def user_follow(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_account = get_object_or_404(UserAccount, username=username)
            user_account.follow(request.user)
            return redirect(
                reverse(
                    "users:user-profile", kwargs={"username": user_account.username}
                )
            )

        messages.error(request, "Method not allowed !")
        return redirect("akromdev:home")

    else:
        messages.info(request, "Please Sign up in system !")
        return redirect(reverse("users:sign-up"))


@login_required
def user_unfollow(request, username):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_account = get_object_or_404(UserAccount, username=username)
            user_account.unfollow(request.user)
            return redirect(
                reverse(
                    "users:user-profile", kwargs={"username": user_account.username}
                )
            )

        messages.error(request, "Method not allowed !")
        return redirect("akromdev:home")

    else:
        messages.info(request, "Please Sign up in system !")
        return redirect(reverse("users:sign-up"))


@login_required
def user_folowers(request, username):
    user_account = get_object_or_404(UserAccount, username=username)
    users = user_account.user.folowers.all()
    return render(request, "user/users.html", {"title": "Folowers", "users": users})


@login_required
def user_folowings(request, username):
    user_account = get_object_or_404(UserAccount, username=username)
    users = user_account.user.folowings.all()
    return render(request, "user/users.html", {"title": "Folowings", "users": users})


__all__ = (
    "user_follow",
    "user_unfollow",
    "user_folowers", 
    "user_folowings",
)