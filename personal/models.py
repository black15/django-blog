from django.db import models
from django.db.models.fields import CharField

# Create your models here.

# class Blog(models.Model):
#     title           = models.CharField(max_length=50)
#     slug            = models.SlugField()
#     body            = models.TextField()
#     date            = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    
#     # change in admin site
#     class Meta:
#         verbose_name = "The Blog"
#         verbose_name_plural = "People's Blogs"