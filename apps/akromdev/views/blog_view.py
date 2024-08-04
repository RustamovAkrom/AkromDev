from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from apps.akromdev.models.blog_model import Post
from apps.akromdev.forms.blog_form import PostUpdateForm, PostCreateForm
from apps.users.models import UserAccount
from django.contrib.auth.mixins import LoginRequiredMixin
import markdown2


class BlogPostView(View):
    def get(self, request):
        if request.user.is_authenticated:
            posts = Post.objects.filter(is_active=True).exclude(
                author=get_object_or_404(UserAccount, user=request.user)
            )

        else:
            posts = Post.objects.filter(is_active=True).order_by("-created_at")

        return render(request, "blog/blogs.html", {"posts": posts})


class BlogPostDetailView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            posts = Post.objects.filter(is_active=True)
            post = posts.get(slug=slug)

            return render(
                request,
                "blog/blog-detail.html",
                {
                    "post_content_html": markdown2.markdown(post.content),
                    "post": post,
                    "posts": posts,
                },
            )

        else:
            return redirect("users:sign-up")


class UserPostView(LoginRequiredMixin, View):
    def get(self, request, username):
        posts = Post.objects.filter(
            author=get_object_or_404(UserAccount, username=username)
        )
        return render(request, "blog/user-posts.html", {"posts": posts})


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "blog/post-create.html", {"form": PostCreateForm()})

    def post(self, request):
        form = PostCreateForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            post = Post.objects.create(
                author=get_object_or_404(UserAccount, user=request.user),
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                content=form.cleaned_data.get("content"),
                is_active=form.cleaned_data.get("is_active"),
            )
            messages.success(request, f"Successfully created post {post.title}")
            return redirect(reverse("akromdev:post-create"))

        messages.error(request, "Your fields are not valid !")
        return redirect(reverse("akromdev:post-create"))


class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        return render(
            request,
            "blog/post-update.html",
            {"form": PostUpdateForm(instance=post), "post": post},
        )

    def post(self, request, slug):
        post = Post.objects.filter(slug=slug)

        form = PostUpdateForm(
            data=request.POST,
            files=request.POST,
            instance=post.first(),
        )
        if form.is_valid():
            post.update(
                author=get_object_or_404(UserAccount, user=request.user),
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                content=form.cleaned_data.get("content"),
                is_active=form.cleaned_data.get("is_active"),
            )

            messages.success(request, f"Successfully created post {post.first().title}")
            return redirect(
                reverse("akromdev:post-update", kwargs={"slug": post.first().slug})
            )

        messages.error(request, "Your fields are not valid !")
        return redirect(reverse("akromdev:post-update", kwargs={"slug": slug}))


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug):
        return render(
            request,
            "blog/post-delete.html",
            {"post": get_object_or_404(Post, slug=slug)},
        )

    def post(self, request, slug):
        get_object_or_404(Post, slug=slug).delete()
        return redirect("akromdev:posts")
