from django.shortcuts import render,redirect
from .forms import RegisterationForm,PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request,'main/home.html')

@login_required(login_url="/login")
def create_post(request):
    if request.method =='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("/home")
        else:
            form=PostForm()
            
    return render(request,'main/create_post.html',{"form":form})


def sign_up(request):
    if request.method =='POST':
        form=RegisterationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=True)
            login(request,user)
            return redirect('/home')
    else:
        form=RegisterationForm()
    
    return render(request,'registration/sign_up.html',{"form":form})