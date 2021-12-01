from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver

# Create your models here.

def upload_dir(instance, filename):
    file_path = f'blog/uploads/{str(instance.author.id)}/{str(instance.title)}-{filename}'
    return file_path

class Blog(models.Model):
    title           = models.CharField(max_length=100, null=False, blank=False)
    body            = models.TextField(max_length=10000, null=False, blank=False)
    image           = models.ImageField(upload_to=upload_dir, null=False, blank=False)
    create_date     = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    update_date     = models.DateTimeField(auto_now=True,verbose_name="date updated")
    author          = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug            = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.title

@receiver(post_delete, sender=Blog)
def submit_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)

pre_save.connect(pre_save_blog_post_reciever, sender=Blog)