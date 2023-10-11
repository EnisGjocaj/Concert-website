from django.urls import path

from . import views

app_name="invitations"

urlpatterns = [
    path('', views.index, name="index"),
    path('/banners/', views.banners, name="banners"),
]