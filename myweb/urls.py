from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    
    path('shop', views.shop, name='shop'),
    path('showorder', views.showorder, name='showorder'),
    path('order', views.order, name='order'),
    path('yourorder', views.yourorder, name='yourorder'),
    path('test', views.test, name='test'),
    path('signUp', views.signUp, name='signUp'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    #path('login_active',views.login_active, name='login_active'),
    path('logIn', views.logIn,name='logIn'),
    

]