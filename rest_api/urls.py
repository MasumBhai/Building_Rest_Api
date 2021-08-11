from django.urls import path
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter

from rest_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='helloviewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.UserLoginApiView.as_view()),
    path('hello-view/', views.HelloApiView.as_view(), name='api-view'),
]
