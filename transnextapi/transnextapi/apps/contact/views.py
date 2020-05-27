from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .models import Faq, Profile, Certifications, Contactus, Culture, Factory, Blog
from .serializers import FaqModelSerializer, ProfileModelSerializer,\
                         CertificationsModelSerializer, ContactusModelSerializer,\
                         FactoryModelSerializer, CultureModelSerializer, BlogModelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class FaqListAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqModelSerializer


class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileModelSerializer


class CertificationsListAPIView(ListAPIView):
    queryset = Certifications.objects.all()
    serializer_class = CertificationsModelSerializer


class ContactusListAPIView(ListAPIView):
    queryset = Contactus.objects.all()
    serializer_class = ContactusModelSerializer


class CultureListAPIView(ListAPIView):
    queryset = Culture.objects.all()
    serializer_class = CultureModelSerializer


class FactoryListAPIView(ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactoryModelSerializer


class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)
