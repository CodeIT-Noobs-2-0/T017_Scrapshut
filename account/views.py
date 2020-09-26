
from .forms import *
from django.db.models import Count
from django.shortcuts import render,redirect,reverse


from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic import DetailView, ListView, TemplateView


from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    return render(request, 'home.html')

@login_required
def base_index(request):
    return render(request,'index.html')



def donorSignup(request):
    if request.method == 'POST':
        form = DonorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            role = form.cleaned_data.get('role')
            #user = authenticate(username=username, password=raw_password)
            print(role)
            login(request, user)
            return redirect('home')
    else:
        form = DonorSignUpForm()
    return render(request, 'signup.html', {'form': form})

def ngo_adminSignup(request):
    if request.method == 'POST':
        form = NGO_Admin_SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            #role = form.cleaned_data.get('role')
            #user = authenticate(username=username, password=raw_password)
            #print(role)
            login(request, user)
            return redirect('home')
    else:
        form = NGO_Admin_SignUpForm()
    return render(request, 'ngoAdminSignup.html', {'form': form})

