from django.shortcuts import render,redirect
from .forms import RegisterationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request,'main/home.html')


def sign_up(request):
    if request.method =='POST':
        form=RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/home')
    else:
        form=RegisterationForm()
    
    return render(request,'registration/sign_up.html',{"form":form})