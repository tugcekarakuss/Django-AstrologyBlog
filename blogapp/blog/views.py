from multiprocessing import context
from django.shortcuts import HttpResponse
from django.shortcuts import render #kaynğı kullanıcıya gönderir.
from blog.models import Blog,Category

def index(request):
    context={
        "blog": Blog.objects.filter(is_active=True,is_home=True),
        "categories": Category.objects.all()
    }
    return render(request,"blog/index.html" , context) #render ile gelen requeste index.html i göster diyor.

def blog(request):
    context={
        "blog": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request,"blog/blog.html", context)

def blog_details(request,slug):
    blog = Blog.objects.get(slug=slug)
    return render(request,"blog/blog-details.html",{
        "blog": blog
    })
    
def blog_by_category(request, slug):
    context={
        "blog": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        # "blog": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request,"blog/blog.html", context)
