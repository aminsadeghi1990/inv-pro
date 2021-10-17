from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import messages

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *
from .models import *

from django.contrib.auth.models import User, auth
from random import randint
from uuid import uuid4

def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'dashboard'

    actual_decorator = user_passes_test(
            lambda u: u.is_anonymous,
            login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def index(request):
    context ={}
    return render(request, 'invapp/index.html', context)

@annonymous_required
def login(request):
    context = {}
    if request.method == 'GET':
        form = UserLoginForm()
        context['form'] = form
        return render(request, 'invapp/login.html', context)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            return redirect('dashboard')
        else:
            print('Credentials not valid')
            context['form'] = form
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'invapp/login.html', context)
@login_required
def dashboard(request):
    context = {}
    return render(request, 'invapp/dashboard.html', context)
