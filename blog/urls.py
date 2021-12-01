from django.urls import path
from django.urls.conf import include
from .views import create_blog, blog_details, edit_blog

urlpatterns = [
    path("create/", create_blog, name="create" ),
    path("<slug>/", blog_details, name="details"),
    path("<slug>/edit", edit_blog, name="edit"),
]
