from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.users.forms.signin_form import SignInForm


class SignInView(View):
    def get(self, request):
        form = SignInForm()
        return render(request, "user/sign_in.html", {"form": form})

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
            )
            login(request, user)

            messages.success(request, f"Successfully registered {user.username}")
            return redirect("akromdev:home")

        messages.error(request, "Your fields are nov valid !")
        return redirect("users:sign-in")

__all__ = ("SignInView", )