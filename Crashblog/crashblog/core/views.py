from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request,'core/frontpage.html',{
        'posts':posts
        })

#-------about-----
def about(request):
    return render(request,'core/about.html')


def robots_txt(request):
    text=[
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")

# #--------------------
# def base(request):
#     posts = Post.objects.all()
#     return render(request,'core/base.html',{
#         'posts':posts
#         })
