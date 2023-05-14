from django.shortcuts import render, redirect
from django.contrib import auth
from user.models import CustomUser as User
# Create your views here.

def login(request):
    #print(request)
    #print(request.method)
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    # print("============ request : ", request)
    # print("============ request : ", request.POST)
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"]
            )
            # print("============ request : ", user)
            authenticated_user = auth.authenticate(
                request,
                username=user.username,
                password=request.POST["password1"]
            )
            # print("============ request : ", authenticated_user)

            if authenticated_user is not None:
                auth.login(request, authenticated_user)
                return redirect('home')
            else:
                return render(request, 'signup.html')
        else:
            return render(request, 'signup.html')
    return render(request, 'register.html')