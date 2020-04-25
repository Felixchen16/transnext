from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerModelSerializer
from transnextapi.settings import constants


# Create your views here.
class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_deleted=False).order_by("-order", "-id")[:constants.BANNER_LENGTH]
    serializer_class = BannerModelSerializer
