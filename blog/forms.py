from django import forms
from django.db import models
from django.db.models import fields
from .models import Blog

class CreateBlog(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('title', 'body', 'image')

class UpdateBlog(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body', 'image')

    def save(self, commit=True):
        
        blog = self.instance
        blog.title = self.cleaned_data['title']
        blog.body = self.cleaned_data['body']
        if self.cleaned_data['image']:
            blog.image = self.cleaned_data['image']

        if commit:
            blog.save()
        
        return blog
    