from django.forms import CharField, TextInput, PasswordInput, ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CreateProduct, Blog
from django import forms

class SignupForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    email = CharField(widget=TextInput(attrs={'placeholder': 'Email'}))
    password1 = CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = CharField(widget=PasswordInput(attrs={'placeholder': 'Confirm password'}))
    
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
    
class CreateproductForm(ModelForm):
    class Meta:
        model = CreateProduct
        fields = ['section', 'title', 'text', 'photo', 'price']
        
class BlogForm(ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add a comment'}))
    class Meta:
        model = Blog
        fields = ['text']