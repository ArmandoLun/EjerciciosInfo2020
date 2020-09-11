from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from polls.forms import *
from polls.models import Post


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})


def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return index(request)
    else:
        form = PostForm()
        return render(request, 'newPost.html', {'form': form})


def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        for fieldname in ['username', 'password1', 'password2']:
            form.fields[fieldname].help_text = None
        context = {'form': form}
        return render(request, 'registration/register.html', context)
