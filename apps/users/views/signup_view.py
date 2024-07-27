from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.users.forms.signup_form import SignUpForm


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, "user/sign_up.html", {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():

            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )
            if user:
                login(request, user)
                messages.success(
                    request, f"{request.user.username} you successfully loged"
                )
                return redirect("akromdev:home")

            messages.error(request, "Invalid username or password !")
            return redirect("users:sign-up")

        messages.warning(request, "Your username or password are not valid !")
        return redirect("users:sign-up")

__all__ = ("SignUpView", )