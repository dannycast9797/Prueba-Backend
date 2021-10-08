
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse




def index(request):
    user = request.user
    return render(request,"login/index.html", {
        'user': user,
    })


def login_view(request):
    if request.method == "POST":

        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
            
        else:
            return render(request, "login/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "login/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

