from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentsForm
# Create your views here.

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    form = CommentsForm()
    if request.method=='POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            #creating temporary comment (not save in DB)

            comment = form.save(commit=False)
            comment.post=post #reffering to post (above)
            comment.save() # then add to DB
            return redirect('post_detail', slug=slug)
    else:
        form = CommentsForm()

    return render(request, 'blog/detail.html', {
        'post':post,
        'form':form
        })

def category(request,slug ):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'blog/category_detail.html', {
        'category':category,
        'posts':posts,
    })

# -----Search menu

def search(request):
    query = request.GET.get('query','')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains = query)
                                | Q(intro__icontains = query)
                                | Q(body__icontains = query))
    return render(request, 'blog/search.html',{
        'posts':posts,
        'query':query,
        })