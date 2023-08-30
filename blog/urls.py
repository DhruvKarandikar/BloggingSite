from django.urls import path
from .views import post_create_view, detail_post_view, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    path('', views.post_create_view, name='blog-home'),
    path('post/<int:id>/', views.detail_post_view, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]



