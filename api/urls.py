from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework import routers
from .views import PostViewSet, AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)

router = SimpleRouter()

router.register('', PostViewSet, basename='posts')
router.register('auth', AuthViewSet, basename='auth')
urlpatterns = router.urls