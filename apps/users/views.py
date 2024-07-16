from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class SignUp(TemplateView):
    template_name = "user/sign_up.html"


class SignIn(TemplateView):
    template_name = "user/sign_in.html"


class SignOut(TemplateView):
    template_name = "user/sign_out.html"


class UserAccountView(View):
    def get(self, request, token):
        return render(request, "user/user_account.html")