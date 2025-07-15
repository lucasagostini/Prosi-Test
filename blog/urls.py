from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, post_list_page, post_detail_page

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = [
    path("", include(router.urls)),  # router first
    path("", post_list_page, name="post_list_page"),
    path("posts/<int:pk>/", post_detail_page, name="post_detail_page"),
]
