from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if ( not email) :
            raise ValueError('Email is Required !')
        if ( not username) :
            raise ValueError('Username is Required !')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    email       = models.EmailField(verbose_name="email", max_length=70, unique=True)
    username    = models.CharField(max_length=30, verbose_name="username", unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="join date")
    last_login  = models.DateTimeField(auto_now=True, verbose_name="last login") 
    is_admin    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
