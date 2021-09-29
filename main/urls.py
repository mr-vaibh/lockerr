from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:long_url>/', views.long_url, name='long_url'),
]