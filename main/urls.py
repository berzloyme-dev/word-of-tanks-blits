from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.home, name='home'),
    path('', views.tank_list, name='tank_list'),
    path('tanks/<slug:slug>/', views.tank_detail, name='tank_detail'),
    path('nation/<slug:slug>/', views.tanks_by_nation, name='nation_detail'),
]
