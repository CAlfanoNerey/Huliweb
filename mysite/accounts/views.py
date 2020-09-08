import datetime
from io import BytesIO

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login

from django.db.backends.utils import logger
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.generic import ListView, DetailView
from xhtml2pdf import pisa

from .forms import RegistrationForm, RegisterUpdateForm, UpdatePasswordForm


from django.views.generic.edit import CreateView, UpdateView
from .models import User, Item

from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import views as auth_views

# Create your views here.
from .utils import render_to_pdf


def indexView(request):
    return render(request, 'index.html')

@login_required()
def dashboardView(request):
    return render(request, 'accounts:dashboard.html')


def logoutview(request):
    return render(request, 'registration/logged_out.html')


class SignUpView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'registration/register.html'


class ViewProfile(generic.DetailView):
    model = User
    template_name = 'profile.html'


def edit_profile(request):
    if request.method == 'POST':
        form = RegisterUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile', pk=request.user.pk)

    else:
        form = RegisterUpdateForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)


@login_required()
def edit_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:view_profile', pk=request.user.pk)
    else:
        form = UpdatePasswordForm()
        args = {'form': form}
        return render(request, 'password.html', args)




def RequesterUpdate(request):
    model = User
    form_class = RegisterUpdateForm()
    template_name = "edit_requester.html"
    success_url = 'profile'




def loginview(request):
    if request.method == "POST":

        context = {}
        form = AuthenticationForm(None, request.POST)
        context['form'] = form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('accounts:home')
    else:
        if request.user.is_authenticated:
            return redirect('accounts:home')
        else:
            ...

        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form}, )


class HomeView(ListView):
    model = Item
    template_name = "index.html"


# def homeView(request):
#     args = {
#         'items': Item.objects.all()
#     }
#     return render(request, "index.html", args)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'

def item_list (request):
    args = {
        'items': Item.objects.all()
    }
    return render(request, "item_list.html", args)


def checkoutPage (request):
    args = {
        'items': Item.objects.all()
    }
    return render(request, "checkout-page.html", args)


def productPage (request):
    args = {
        'items': Item.objects.all()
    }
    return render(request, "product-page.html", args)