from django.urls import path
from . import views
urlpatterns = [
    path(r"faq/", views.FaqListAPIView.as_view()),
    path(r"profile/", views.ProfileListAPIView.as_view()),
    path(r"certifications/", views.CertificationsListAPIView.as_view()),
    path(r"contactus/", views.ContactusListAPIView.as_view()),
    path(r"culture/", views.CultureListAPIView.as_view()),
    path(r"factory/", views.FactoryListAPIView.as_view()),
    path(r"blog/", views.BlogListAPIView.as_view()),
]
