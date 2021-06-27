from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Patient
from .forms import AuthenticationForm,RegistrationForm

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
#just a litle decorator that checks if user is loged in if he is goes to profile else it performs the view
def no_user_required(view):
    def wrapper(request):
        if request.user.is_authenticated:
            return redirect('/chat')
        else:
            return view(request)
    return wrapper


@login_required(login_url='/auth/')
def home(request):
    return render(request ,'user/index.html')

@no_user_required
def login_view(request):

    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    request,
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password')
                )
                if user is None:
                    messages.error(request,'Login failed! password or email are incorrect')
                else:
                    name = user.client_name
                    messages.success(request , 'Welcome {}'.format(name))
                    login(request,user)
                    return redirect('/chat')
            else:
                messages.error(request,'Login failed!')
        if 'register' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                raw_password = form.cleaned_data.get('password')
                user = form.save()
                _user = authenticate(request,email=email,password=raw_password)
                login(request, user)
                return redirect('/chat')
            else:
                messages.error(request,'Registration failed!')
    return render(request , 'user/login.html')

@login_required(login_url='/auth/')
def logout_view(request):
    logout(request)
    messages.info(request,'Logout successful!')
    return redirect('/')
