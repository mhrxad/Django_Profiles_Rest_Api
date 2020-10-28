from django.urls import path, include
from profiles_api_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfilFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginapiView.as_view()),
    path('', include(router.urls))
]
