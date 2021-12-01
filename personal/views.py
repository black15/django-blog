from django.shortcuts import render
from operator import attrgetter
from blog.models import Blog

# Create your views here.

def home(request):

    blogs = sorted( Blog.objects.all() , key=attrgetter('update_date') , reverse=True)
    

    context = {
        "blogs": blogs,
        "title": "Home",
    }


    return render(request, 'personal/home.html', context)

# def blogs(request):
#     blogs = Blog.objects.all()

#     context = {
#         "blogs": blogs,
#     }

#     return render(request, 'personal/blogs.html', context)