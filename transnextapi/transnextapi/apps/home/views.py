from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Banner, Nav, Menu, MainBanner, CenterBanner, Message
from .serializers import BannerModelSerializer, NavModelSerializer, MainBannerModelSerializer, \
    CenterBannerModelSerializer, MessageModelSerializer
from transnextapi.settings import constants


# Create your views here.
class BannerListAPIView(ListAPIView):
    """轮播广告视图"""
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("order", "id")[
               :constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer


class MenuNavListAPIView(ListAPIView):
    """导航菜单视图"""
    queryset = Nav.objects.filter(is_show=True, is_deleted=False).order_by("order", "id")
    serializer_class = NavModelSerializer


class MainBannerListAPIView(ListAPIView):
    """横幅广告视图"""
    queryset = MainBanner.objects.filter(is_show=True, is_deleted=False).order_by("order", "id")[
               :constants.MAIN_BANNER_LENGTH]
    serializer_class = MainBannerModelSerializer


class CenterBannerListAPIView(ListAPIView):
    """中间广告视图"""
    queryset = CenterBanner.objects.filter(is_show=True, is_deleted=False).order_by("order", "id")[
               :constants.CENTER_BANNER_LENGTH]
    serializer_class = CenterBannerModelSerializer


class MessageCreateAPIView(CreateAPIView):
    """留言板视图"""
    serializer_class = MessageModelSerializer
