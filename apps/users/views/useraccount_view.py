from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from apps.users.forms.useraccount_form import UserAccountForm
from apps.users.models.useraccount_model import UserAccount


class UserAccountView(LoginRequiredMixin, View):
    def get(self, request):
        user_account = get_object_or_404(UserAccount, user=request.user)
        form = UserAccountForm(instance=user_account)

        return render(
            request,
            "user/user_account.html",
            {"form": form, "user_account": user_account},
        )

    def post(self, request):
        user_account = get_object_or_404(UserAccount, user=request.user)

        form = UserAccountForm(
            data=request.POST, files=request.FILES, instance=user_account
        )
        if form.is_valid():
            form.save()

            messages.success(
                request, f"Successfully updated your account {request.user.username}"
            )
            return redirect("users:user-account")

        messages.error(request, "You`r fields are not valid !")
        return redirect("users:user-account")

__all__ = ("UserAccountView", )