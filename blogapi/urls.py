from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="blog/post_list.html"), name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("blog.urls")),
]
