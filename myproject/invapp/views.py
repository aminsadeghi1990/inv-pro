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
@login_required
def invoices(request):
    context = {}
    return render(request, 'invapp/invoice.html', context)
@login_required
def products(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'invapp/products.html', context)
@login_required
def clients(request):
    context = {}
    clients = Client.objects.all()
    context['clients'] = clients

    if request.method == 'GET'
        form = ClientForm()
        context['form'] = form
        return render(request, 'invapp/clients.html', context)
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
@login_required
def createInvoice(request):
    number = 'INVNUM'+str(uuid4()).split('-')[1]
    newInvoice = Invoice.object.create(number=number)
    newInvoice.save()
    inv = Invoice.objects.get(nimber = number)
    return redirect(request, 'invapp/create-invoice.html')
       
   
def createBuildInvoice(request, slug):
    try:
        invoice = Invoice.objects.get(slug=slug)
    except:
        message.error(request, 'called object not found!!')
        return redirect('invoices')
    products = Product.objects.filter(invoice=invoice)

    context = {}
    context['invoice'] = invoice
    context['products'] = products
    if request.method == 'GET':
         prod_form = ProductForm()
         inv_form = InvoiceForm()
         context['prod_form'] = prod_form
         context['inv_form'] = prod_form
         return redirect(request, 'invapp/create-build-invoice.html', context)
   return render(request, 'invoice/create-invoice.html', context)

