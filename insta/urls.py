from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
    # path('public/', views.public_post_list),
    path('', include(router.urls)),
]
