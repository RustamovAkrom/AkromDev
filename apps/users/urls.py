from django.urls import path
from .views import (
    SignUpView,
    SignInView,
    SignOutView,
    UserAccountView,
    UserProfileView,
    user_follow,
    user_unfollow,
    user_folowers,
    user_folowings,
)


app_name = "users"

urlpatterns = [
    path("sign_up/", SignUpView.as_view(), name="sign-up"),
    path("sign-in/", SignInView.as_view(), name="sign-in"),
    path("sign-out/", SignOutView.as_view(), name="sign-out"),
    path("akromdev-user-account/", UserAccountView.as_view(), name="user-account"),
    path(
        "akromdev-user-profile/<str:username>",
        UserProfileView.as_view(),
        name="user-profile",
    ),
    path("user-follow/<str:username>", user_follow, name="user-follow"),
    path("user-unfollow/<str:username>", user_unfollow, name="user-unfollow"),
    path("user-folowers/<str:username>", user_folowers, name="user-folowers"),
    path("user-folowings/<str:username>", user_folowings, name="user-folowings"),
]
