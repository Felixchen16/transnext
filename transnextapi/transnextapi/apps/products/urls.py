from django.urls import path, re_path
from . import views
urlpatterns = [
    path(r"products/", views.ProductsListAPIView.as_view()),
]
