from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import  logout, login, authenticate
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class LoginView(View):
    def post(self, request):
        user = authenticate(
            username = request.POST.get("l"),
            password = request.POST.get("p")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/asosiy/bolimlar/")
    def get(self, request):
        return render(request, 'home.html')

