from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime as dt
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .email import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):
    posts = Post.all_posts()
    profile = Profile.get_all_profiles()
    comments=Comment.objects.all()
    current_user = request.user
     if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('homepage')

    else:
        form=CommentForm
    context =  {
        "profile": profile,
        "form": form,
        "posts":posts ,
        "comments":comments,
    }
    return render(request, 'images/homepage.html', context)

@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_profile = current_user
            post.save()
        return redirect('homepage')

    else:
        form = UploadForm()
    return render(request, 'images/upload.html', {"form": form})

def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    images = Post.get_profile_image(profile.id)
    title = f'@{profile.username}'
    return render(request, 'images/profile.html', {'title':title, 'profile':profile, 'profile_info':profile_info, 'images':images})    