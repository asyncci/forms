from django.shortcuts import render
from .models import Post
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
from .forms import PostForm
from django.urls import reverse
from django.views.generic.edit import CreateView,UpdateView

def posts(request):
    posts = Post.objects.all()
    return render(request,"fillup/posts.html",context={'posts':posts})

def post(request, id):
    post = Post.objects.get(pk=id)
    return render(request,"fillup/post.html",context={'post':post})


class AddPost(CreateView):
    # model = Books
    form_class = PostForm
    template_name = "fillup/add_post.html"
    def get_success_url(self):
        return reverse('posts')

def delete(request,id):
    post = Post.objects.get(pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('posts'))

class PostUpdate(UpdateView):
    model = Post
    template_name = "fillup/update.html"
    fields = ['title' , 'description' , 'price' , 'image']
    def get_success_url(self):
        return reverse('posts')