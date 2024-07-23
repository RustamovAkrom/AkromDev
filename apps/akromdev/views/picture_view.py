from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.views.generic import DeleteView
from django.contrib import messages
from apps.akromdev.models.picture_model import Picture
from apps.akromdev.forms.picture_form import PictureCreateForm, PictureUpdateForm
from apps.users.models import UserAccount
from apps.akromdev.utils import is_photo


class PictureView(ListView):
    model = Picture
    template_name = "picture/pictures.html"
    context_object_name = "pictures"


class PictureDetailView(View):
    def get(self, request, slug):
        pictures = Picture.objects.all().order_by("-created_at")
        picture = pictures.get(slug=slug)
        return render(request, "picture/picture-detail.html", {
            "picture": picture,
            "pictures": pictures
        })


class PictureCreateView(View):
    def get(self, request):
        form = PictureCreateForm()
        return render(request, "picture/picture-create.html", {
            "form": form
        })

    def post(self, request):
        form = PictureCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            image = form.cleaned_data.get("image")

            if is_photo(str(image.name)):
                Picture.objects.create(
                    author = UserAccount.objects.get(user=request.user),
                    image = image,
                    description = form.cleaned_data.get("description"),
                )
                messages.success(request, "Successfully created picture")
                return redirect("akromdev:picture-create")
            
            messages.error(request, "Your phot are not valid !")
            return redirect("akromdev:picture-create")
        
        messages.error(request, "Error in your fields !")
        return redirect("akromdev:picture-create")


class PictureUpdateView(View):
    def get(self, request, slug):
        picture = Picture.objects.get(slug = slug)
        form = PictureUpdateForm(instance=picture)
        return render(request, "picture/picture-update.html", {
            "form": form,
            "picture": picture
        })

    def post(self, request, slug):
        picture = Picture.objects.filter(slug = slug)
        form = PictureUpdateForm(
            data=request.POST,
            instance=picture.first(),
        )
        if form.is_valid():
            picture.update(
                author = UserAccount.objects.get(user = request.user),
                description = form.cleaned_data.get("description"),
            )

            messages.success(request, "Successfully updated picture")
            return redirect(reverse("akromdev:picture-update", kwargs={"slug": picture.first().slug}))
        
        messages.error(request, "Your fields are not valid !")
        return redirect(reverse("akromdev:picture-update", kwargs={"slug": picture.first().slug}))
    

class PictureDeleteView(DeleteView):
    def get(self, request, slug):
        return render(request, "picture/picture-delete.html", {
            "picture": Picture.objects.get(slug = slug)
        })
    
    def post(self, request, slug):
        Picture.objects.get(slug = slug).delete()
        return redirect("akromdev:pictures")