from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('logIn', views.logIn_page ),
    path('shop', views.shop, name='shop'),
    path('order', views.order, name='order'),
    path('test', views.test, name='test'),
    path('signUp', views.signUp, name='signUp'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login_active',views.login_active, name='login_active'),

]