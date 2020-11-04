from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.Post.as_view()),
    path('post/<str:post_id>/', views.PostDetail.as_view()),
]