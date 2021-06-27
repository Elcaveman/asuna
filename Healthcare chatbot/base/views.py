from django.shortcuts import render
from user.views import no_user_required
from django.contrib.auth.decorators import login_required

@no_user_required
def about(request):
    context = {"location":"about"}
    return render(request,"base/about.html",context)

@login_required(login_url='/auth/')
def chat(request):
    context = {"location":"chat"}
    return render(request,"base/chat.html",context)

@no_user_required
def home(request):
    context = {"location":"home"}
    return render(request,"base/home.html",context)