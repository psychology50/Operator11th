from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('blogs/<int:blog_pk>/posts/', views.post_create, name='post_create'),  # POST -> create
    path('blogs/<int:blog_pk>/posts/', views.post_list, name='post_list'),  # GET -> list
    path('blogs/<int:blog_pk>/posts/<int:pk>/', views.post_detail, name='post_detail'),  # GET -> detail
    path('blogs/<int:blog_pk>/posts/<int:pk>/', views.post_update, name='post_update'),  # PATCH -> update (put과 patch 차이)
    path('blogs/<int:blog_pk>/posts/<int:pk>/', views.post_delete, name='post_delete'),  # DELETE -> delete
]