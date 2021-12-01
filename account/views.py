from django.shortcuts import render, redirect
from django.contrib.auth import forms, login, authenticate, logout
from account.forms import RegistrationForm, LoginForm, AccountForm
from account.models import Account
from blog.models import Blog

# Create your views here.

def registration_screen(request):

    if (request.POST):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')

            account = authenticate(email=email, password=raw_password)
            login(request, account)
    
            return redirect('home_screen')

        else:
            context = {
                "registration_form": form,
            }
    else:
        form = RegistrationForm()

        context = {
                "registration_form": form,
            }

    return render(request, 'account/register.html', context)

def login_screen(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home_screen')

    if (request.POST):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home_screen')

        else:
                context['login_form'] = form
    
    else:
        form = LoginForm()
        context['login_form'] = form

    return render(request, 'account/login.html', context)

def account_screen(request):

    context = {}

    if not request.user.is_authenticated:
        return redirect('login')

    if (request.POST):
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            context['change_succ'] = "Username changed succesfully !"
        else:
            form = AccountForm(
                initial={
                    "username": request.user.username,
                }
            )
        context['account_form'] = form

    blogs = Blog.objects.filter(author=request.user)
    context['blogs'] = blogs

    return render(request, 'account/account.html', context)

def logout_screen(request):
    logout(request)
    return redirect('home_screen')