from django.shortcuts import render, redirect
from .models import Statistika
from django.views import View
from accounts.models import *
from asosiy.models import *
class StatistikaView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                "stats": Statistika.objects.filter(ombor=request.user),
                "mahsulot": Mahsulot.objects.filter(ombor=request.user),
                "mijoz": Mijoz.objects.filter(ombor=request.user),
            }
            return render(request, 'stats.html', data)
        return redirect("login")
    def post(self, request):
        Statistika.objects.filter(ombor=request.user).create(
            mahsulot=Mahsulot.objects.get(id=request.POST.get("pr")),
            mijoz=Mijoz.objects.get(id=request.POST.get("m")),
            miqdor=request.POST.get('miqdor'),
            summa=request.POST.get('summa'),
            tanlangan_summa=request.POST.get('tolandi'),
            nasiya=request.POST.get('nasiya'),
            ombor=request.POST.user
        )
        return redirect('/stats/')

