from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, models
from django.forms import fields
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text="Email Required .")

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = Account # What kind of field is excepting to see in the form
        fields = ('email', 'password') # Which fields are going to be visible

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
    
class AccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('username',)
    
    def clear_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try :
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username already exists')
