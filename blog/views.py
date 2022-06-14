import email
from email import message
from django.shortcuts import render
from .models import Blog ,Tag , Category ,Comments
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 1)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)
    context = {
        "blog_list":blog_list,
    }
    return render(request,'blog/blog_list.html' , context)

def blog_detail(request , id):
    blogs = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(tag = blogs)
    recent = Blog.objects.all().order_by("-created_at")
    category = Category.objects.all().filter(blog=blogs)
    comment = Comments.objects.all().filter(blog=blogs)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name =form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_message = form .cleaned_data['message']
            
            new_comment =Comments(blog = blogs, name=new_name , email = new_email , message = new_message)
            new_comment.save()
    return render(request, 'blog/blog_detail.html',{"blogs":blogs , "tags":tags , "recent":recent ,"category":category ,"comment":comment})


def tag_blog(request,tag):
    blogs=Blog.objects.filter(tags__slug=tag)
    
    return render(request,'blog/blog_list.html',{"blog_list":blogs})

def category_blog(request,category):
    blogs = Blog.objects.filter(category__slug=category)
    
    return render(request,'blog/blog_list.html',{"blogs":blogs})

def search(request):
    if request.method =='GET':
        q = request.GET.get("search")
        
    blog_list = Blog.objects.filter(title__icontains = q)
    return render(request,'blog/blog_list.html' , {"blog_list":blog_list})