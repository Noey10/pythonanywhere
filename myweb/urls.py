from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('logIn', views.logIn_page, ),
    path('shop', views.shop, name='shop'),
    path('index1', views.index1, name='index1'),
    path('signUp', views.signUp, name='signUp'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login_active',views.login_active, name='login_active'),

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]