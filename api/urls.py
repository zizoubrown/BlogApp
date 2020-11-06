from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('post/<int:pk>', PostDetail.as_view()),
    path('post', PostList.as_view()),
]