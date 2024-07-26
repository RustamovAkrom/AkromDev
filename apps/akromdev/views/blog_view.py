from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.urls import reverse
from apps.akromdev.models.blog_model import Post
from apps.akromdev.forms.blog_form import PostUpdateForm, PostCreateForm
from apps.users.models import UserAccount


class BlogPostView(View):
    def get(self, request):
        posts = Post.objects.filter(is_active=True)
        return render(request, "blog/blogs.html", {
            "posts": posts
        })
    

class BlogPostDetail(View):
    def get(self, request, slug):
        posts = Post.objects.filter(is_active=True)
        post = posts.get(slug = slug)
        return render(request, "blog/blog-detail.html", {
            "post": post,
            "posts": posts
        })
     

class PostCreateView(View):
    def get(self, request):
        return render(request, "blog/post-create.html", {
            "form": PostCreateForm()
        })

    def post(self, request):
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = Post.objects.create(
                author = UserAccount.objects.get(user = request.user),
                title = form.cleaned_data.get("title"),
                bg_image = form.cleaned_data.get("bg_image"),
                description = form.cleaned_data.get("description"),
                content = form.cleaned_data.get("content"),
                is_active = form.cleaned_data.get("is_active")
            )
            messages.success(request, f"Successfully created post {post.title}")
            return redirect(reverse("akromdev:post-create"))
        
        messages.error(request, "Your fields are not valid !")
        return redirect(reverse("akromdev:post-create"))


class PostUpdateView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug = slug)
        return render(request, "blog/post-update.html", {
            "form": PostUpdateForm(instance=post),
            "post": post
        })

    def post(self, request, slug):
        post = Post.objects.filter(slug = slug)
        form = PostUpdateForm(
            data=request.POST,
            files=request.POST,
            instance=post.first(),
        )
        if form.is_valid():
            post.update(
                author = UserAccount.objects.get(user = request.user),
                title = form.cleaned_data.get("title"),
                bg_image = form.cleaned_data.get("bg_image"),
                description = form.cleaned_data.get("description"),
                content = form.cleaned_data.get("content"),
                is_active = form.cleaned_data.get("is_active"),
            )
            
            messages.success(request, f"Successfully created post {post.first().title}")
            return redirect(reverse("akromdev:post-update", kwargs={"slug": post.first().slug}))
        
        messages.error(request, "Your fields are not valid !")
        return redirect(reverse("akromdev:post-update", kwargs={"slug":slug}))


class PostDeleteView(View):
    def get(self, request, slug):
        return render(request, "blog/post-delete.html", {
            "post": Post.objects.get(slug = slug)
        })
    
    def post(self, request, slug):
        Post.objects.get(slug = slug).delete()
        return redirect("akromdev:posts")