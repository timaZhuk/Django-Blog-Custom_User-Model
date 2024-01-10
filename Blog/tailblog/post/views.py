from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment, Category

#----- Create your views here.

def frontpage(request):
    posts = Post.objects.all()
    return render(request,'post/frontpage.html',{
        'posts':posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method=='POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        comment = request.POST.get('comment','')
    #------------If all fields are completed---------------------------
        if name and comment:
            Comment.objects.create(
                post=post,
                name=name,
                comment=comment,

            )
            return redirect('post_detail', slug = post.slug)

    return render(request, 'post/post_detail.html',{
        'post':post
    })

#------------category detail----------------------
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)

    return render(request, 'post/category_detail.html',{
        'category':category,
    })