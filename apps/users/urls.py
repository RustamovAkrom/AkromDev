from django.urls import path
from .views import SignUp, SignIn, SignOut, UserAccountView

app_name = "users"

urlpatterns = [
    path("sign_up/", SignUp.as_view(), name="sign-up"),
    path("sign-in/", SignIn.as_view(), name="sign-in"),
    path("sign-out/", SignOut.as_view(), name="sign-out"),
    path("akromdev-user-account/<str:token>", UserAccountView.as_view(), name="user-account")
]