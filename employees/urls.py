
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from employees import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('course',views.CourseViewSet)
router.register('user',views.UserViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]