from django.urls import path
from .views import SignUp, SignIn, SignOut, UserAccountView, UserProfileView

app_name = "users"

urlpatterns = [
    path("sign_up/", SignUp.as_view(), name="sign-up"),
    path("sign-in/", SignIn.as_view(), name="sign-in"),
    path("sign-out/", SignOut.as_view(), name="sign-out"),
    path("akromdev-user-account/", UserAccountView.as_view(), name="user-account"),
    path("akromdev-user-profile/<str:username>", UserProfileView.as_view(), name="user-profile"),
]