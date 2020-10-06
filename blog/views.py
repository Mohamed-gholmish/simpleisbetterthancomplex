from django.shortcuts import render
from .models import Post

# Create your views here.
def all_posts(request):
    all_posts=Post.objects.all()

    return render(request,'blog/all_posts.html',{'posts':all_posts})

def post_detail(request,post_id):
    single_post=Post.objects.get(id=post_id)

    return render(request,'blog/post_detail.html',{'post':single_post})
