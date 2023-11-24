from django.shortcuts import render, redirect
from .models import *
from django.views import View


class BolimlarView(View):
    def get(self, request):
        return render(request, 'bulimlar.html')

    def post(self, request):
        pass


class MahsulotlarView(View):

    def post(self, request):
        Mahsulot.objects.create(
            nom=request.POST.get('pr_name'),
            brend=request.POST.get('pr_brand'),
            narx=request.POST.get('pr_price'),
            miqdor=request.POST.get('pr_amount'),
            ombor=request.user
        )
        return redirect('bolimlar/mahsulotlar/')
    def get(self, request):
        data = {
            "mahsulotlar" : Mahsulot.objects.filter(ombor=request.user)
        }
        return render(request, 'products.html', data)

class MijozlarView(View):
    def post(self, request):
        Mijoz.objects.create(
            ism=request.POST.get('client_name'),
            nom=request.POST.get('client_shop'),
            manzil=request.POST.get('client_address'),
            tel=request.POST.get('client_phone'),
            ombor=request.user
        )
        return redirect('asosiy/clientlar/')
    def get(self, request):
        data = {
            "mijozlar" : Mijoz.objects.filter(ombor=request.user)
        }
        return render(request, 'clients.html', data)

class Mahsulotlar_updateView(View):
    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            nom=request.POST.get("name"),
            brend=request.POST.get("brand_name"),
            narx=request.POST.get("price"),
            miqdor=request.POST.get("amount"),
        )
        return redirect('/asosiy/bolimlar/mahsulotlar/')

    def get(self, request, pk):
        product = Mahsulot.objects.get(id=pk)
        if request.user.is_authenticated and request.user == product.ombor:
            data = {
                "product" : product
            }
            return render(request, 'product_update.html', data)

class Clients_updateView(View):
    def post(self, request, son):
        Mijoz.objects.filter(id=son)
        