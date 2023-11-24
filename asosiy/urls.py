from django.urls import path
from .views import *
from stats.views import StatistikaView
urlpatterns = [
    path("bolimlar/", BolimlarView.as_view()),
    path("bolimlar/mahsulotlar/", MahsulotlarView.as_view()),
    path("bolimlar/clientlar/", MijozlarView.as_view()),
    path("mahsulotlar_update/<int:pk>/", Mahsulotlar_updateView.as_view()),

]