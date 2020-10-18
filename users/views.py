from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Category
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

# Create your views here.
def home(request):
    contexts = {
        'categories':Category.objects.all()
    }
    return render(request,'users/home.html',contexts)

def login(request):
    return render(request,'users/login.html')

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created. You will now be able to successfully login.')
            return redirect('login-page')
    else:
        form = UserRegisterForm()
    return render(request,'users/registeration.html',{'form':form})

def logout(request):
    return render(request,'users/logout.html')

@login_required
def search(request):
    return render(request,'users/search.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has beeen updated!!!')
            return redirect('profile-page')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    contexts = {
        'p_form':p_form,
        'u_form':u_form,
    }
    return render(request,'users/profile.html',contexts)
