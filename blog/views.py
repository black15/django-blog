from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateBlog, UpdateBlog
from account.models import Account
from .models import Blog

# Create your views here.

def create_blog(request):

    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('login')
    
    if request.POST:
        form = CreateBlog(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = Account.objects.filter(email=user.email).first()
            obj.author = author
            obj.save()
            form = CreateBlog()

            context['succs'] = "Blog created succesfully !"
            
        context['form'] = form

    return render(request, 'blog/create_blog.html', context)

def blog_details(request, slug):
    
    context = {}

    queryset = Blog.objects.filter(author=request.user)
    blog = get_object_or_404(queryset, slug=slug)
    context['blog'] = blog
    
    return render(request, 'blog/blog_details.html', context)

def edit_blog(requset, slug):

    context = {}

    user = requset.user
    if not user.is_authenticated:
        return redirect(requset, 'login')
    
    blog = get_object_or_404(Blog, slug=slug)

    if requset.POST:

        form = UpdateBlog(requset.POST or None, requset.FILES or None, instance=blog)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['succs'] = 'Upadted Succesfully !'
            blog = obj
        
    form = UpdateBlog(
        initial={
            "title": blog.title,
            "body": blog.body,
            "image": blog.image,
        }
    )

    context['form'] = form

    return render(requset, 'blog/edit_blog.html', context)
