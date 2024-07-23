from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from apps.akromdev.forms.contact_form import ContactForm
from apps.akromdev.tasks import send_email_task


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, "contact.html", {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            email = form.cleaned_data.get("email")

            send_email_task(subject, message, email)

            messages.success(request, "Successfully sending message")
            return redirect("akromdev:contact")

        messages.error(request, "Your sending message is are not valid !")
        return redirect("akromdev:contact")
