from django.urls import path
from . import views
urlpatterns = [
    path(r"banner/", views.BannerListAPIView.as_view()),
    path(r"nav/menu/", views.MenuNavListAPIView.as_view()),
    path(r"main/banner/", views.MainBannerListAPIView.as_view()),
    path(r"main/center/banner/", views.CenterBannerListAPIView.as_view()),
    path(r"message/", views.MessageCreateAPIView.as_view()),
]
