from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class SignOutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "user/sign_out.html")

    def post(self, request):
        logout(request)
        messages.info(request, "Sign out on system. ")
        return redirect("akromdev:home")


__all__ = ("SignOutView", )