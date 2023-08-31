from django.shortcuts import render,reverse,get_object_or_404
from blog.models import Post, Category, Tag
from blog.forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'index.html', context)


def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # messages.add_message(request, messages.INFO,"Your Post Create Succesfully")
        return HttpResponseRedirect(reverse("blog:index"))
    
    messages.success(request,"Your Post Create Succesfully")
    context = {"form":form}
    return render(request, 'add_post.html', context)


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("blog:index"))
    context = {"form": form}
    return render(request, 'edit_post.html', context)



def delete_post(request):
    post_id = request.POST.get("post_id")
    post = get_object_or_404(Post, id=post_id, user=request.user)
    post.delete()
    messages.add_message(request, messages.INFO, "Delete")
    return HttpResponseRedirect(reverse("blog:index"))