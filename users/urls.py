from django.urls import include, path
from . import views


urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('profile/', views.profile, name='profile'),
]

