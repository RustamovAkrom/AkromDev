from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


from .forms import SignUpForm, SignInForm, UserAccountForm
from .models import User, UserAccount
from apps.akromdev.models import Video, Picture, Audio


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "user/sign_up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():

            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            if user:
                login(request, user)
                messages.success(request, f"{request.user.username} you successfully loged")
                return redirect("akromdev:home")
                
            messages.error(request, "Invalid username or password !")
            return redirect("users:sign-up")
        
        messages.warning(request, "Your username or password are not valid !")
        return redirect("users:sign-up")


class SignIn(TemplateView):
    def get(self, request):
        form = SignInForm()
        return render(request, "user/sign_in.html", {"form": form})
    
    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            login(request, user)

            messages.success(request, f"Successfully registered {user.username}")
            return redirect("akromdev:home")
        
        messages.error(request, "Your fields are nov valid !")
        return redirect("users:sign-in")
    

class SignOut(LoginRequiredMixin, TemplateView):
    def get(self, request):
        return render(request, "user/sign_out.html")

    def post(self, request):
        logout(request)
        messages.info(request, "Sign out on system. ")
        return redirect("akromdev:home")


class UserAccountView(LoginRequiredMixin, View):
    def get(self, request):
        user_account = get_object_or_404(UserAccount, user = request.user)
        form = UserAccountForm(instance=user_account)

        return render(request, "user/user_account.html", {
            "form": form,
            "user_account": user_account
        }) 

    def post(self, request):
        user_account = get_object_or_404(UserAccount, user = request.user)

        form = UserAccountForm(data=request.POST, files=request.FILES, instance=user_account)
        if form.is_valid():
            form.save()

            messages.success(request, f"Successfully updated your account {request.user.username}")
            return redirect("users:user-account")

        messages.error(request, "You`r fields are not valid !")
        return redirect("users:user-account")
    

class UserProfileView(View):
    def get(self, request, username): 
        if username[0] == "@":

            user = User.objects.get(username = username[1:])
            user_account = UserAccount.objects.get(user = user)
            videos = Video.objects.filter(author = user_account).order_by("-created_at")
            audios = Audio.objects.filter(author = user_account).order_by("created_at")
            pictures = Picture.objects.filter(author = user_account).order_by("-created_at")

            return render(request, "user/user_profile.html", {
                "user_account": user_account,
                "videos": videos,
                "audios": audios,
                "pictures": pictures
            })
        
        messages.error(request, "Now validate username not found '@' ")
        return redirect("akromdev:videos")

    def post(self, request, username):
        return 
