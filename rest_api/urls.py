from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('hello-view/', views.HelloApiView.as_view(), name='api-view'),
]
