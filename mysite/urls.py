from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myweb/', include('myweb.urls')),
    path('admin/', admin.site.urls),
]
