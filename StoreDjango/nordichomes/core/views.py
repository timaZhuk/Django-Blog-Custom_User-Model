from django.contrib.auth import login
from django.db.models import Q 
from django.shortcuts import render, redirect
from product.models import Product, Category
from .forms import SignUpForm 
# Create your views here.

#-----FRONT PAGE-------
def frontpage(request):
    products = Product.objects.all()[0:8]
    return render(request,'core/frontpage.html',
                  {'products':products})

#----------SIGN UP -------------------------------------
def signup(request):
    form = SignUpForm() # creating empty instance of form
    # ----creating sign up form
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save() # create the user if form valid
            login(request, user)  #built-in method that login new user
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request,'core/signup.html',
                  {'form':form})

#----------Log in -------------------------------------
def login_old(request):
    return render(request,'core/login.html')

#-----SHOP PAGE-------------
def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    #--- parameter for active category
    active_category = request.GET.get('category','')
    # ----filtering products by category
    if active_category:
        products = products.filter(category__slug = active_category)
    #--- query search
    query = request.GET.get('query','')
    if query:
        products = products.filter(Q(name__icontains=query)
                                   |Q(description__icontains=query))
    #---- new dictionary
    context = {
        'products':products,
        'categories':categories,
        'active_category':active_category
    }

    return render(request,'core/shop.html',
                  context)

