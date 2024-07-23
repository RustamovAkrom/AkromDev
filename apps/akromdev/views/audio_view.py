from django.views import View
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from apps.akromdev.models.audio_model import Audio, AudioCategory
from apps.akromdev.forms.audio_form import AudioCreateForm, AudioUpdateForm
from apps.users.models import UserAccount
from apps.akromdev.utils import is_photo, is_audio


class AudioView(View):
    def get(self, request):
        audios = Audio.objects.all().order_by("-created_at")
        return render(request, "audio/audios.html", {"audios": audios})


class AudioDetailView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            audio = Audio.objects.get(slug=slug)
            audios = Audio.objects.filter(category=audio.category).order_by(
                "-created_at"
            )
            return render(
                request, "audio/audio-detail.html", {"audio": audio, "audios": audios}
            )
        return redirect("users:sign-up")


class AudioCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = AudioCreateForm()
        return render(request, "audio/audio-create.html", {"form": form})

    def post(self, request):
        form = AudioCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            cover = form.cleaned_data.get("cover")
            audio = form.cleaned_data.get("audio")

            if is_photo(cover.name):
                if is_audio(audio.name):
                    Audio.objects.create(
                        author=UserAccount.objects.get(user=request.user),
                        title=form.cleaned_data.get("title"),
                        description=form.cleaned_data.get("description"),
                        category=form.cleaned_data.get("category"),
                        cover=cover,
                        audio=audio,
                    )
                    messages.success(request, "Successfully created audio.")
                    return redirect("akromdev:audio-create")
                
                messages.warning(request, "Your audio are not valid !")
                return redirect("akromdev:audio-create")
            
            messages.warning(request, "Your phot are not valid !")
            return redirect("akromdev:audio-create")
        
        messages.error(request, "Your fields are not valid")
        return redirect("akromdev:audio-create")


class AudioUpdateView(View):
    def get(self, request, slug):
        audio = Audio.objects.get(slug = slug)
        form = AudioUpdateForm(instance=audio)
        return render(request, "audio/audio-update.html", {
            "form": form,
            "audio": audio
        })

    def post(self, request, slug):
        audio = Audio.objects.filter(slug = slug)

        form = AudioUpdateForm(
            data=request.POST, 
            instance=audio.first(),
        )
        if form.is_valid():
            audio.update(
                title = form.cleaned_data.get("title"),
                description = form.cleaned_data.get("description"),
                category = form.cleaned_data.get("category")
            )
                    
            messages.success(request, "Successfully updated Audio.")
            return redirect(reverse("akromdev:audio-update", kwargs={"slug": audio.first().slug}))
        
        messages.error("Your fields are not valid !")
        return redirect(reverse("akromdev:audio-update", kwargs={"slug": audio.first().slug}))


class AudioDeleteView(DeleteView):
    def get(self, request, slug):
        return render(request, "audio/audio-delete.html", {
            "audio": Audio.objects.get(slug = slug)
        })

    def post(self, request, slug):
        Audio.objects.get(slug = slug).delete()
        return redirect("akromdev:audios")