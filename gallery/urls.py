from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_list, name='gallery'),
    path('<int:pk>/', views.gallery_detail, name='gallery_detail'),
]