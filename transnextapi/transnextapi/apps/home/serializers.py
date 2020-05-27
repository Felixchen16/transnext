from rest_framework import serializers
from .models import Banner, Nav, Menu, MainBanner, Message


class BannerModelSerializer(serializers.ModelSerializer):
    """轮播广告的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Banner
        fields = ["image_url", "link"]


class NavModelSerializer(serializers.ModelSerializer):
    """导航菜单的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Nav
        fields = ["id", "title", "link", "is_site"]

    def to_representation(self, instance):
        """
        自定义序列化
        obj：获取每个类别
        children：根据类别获得二级菜单
        """
        obj = Nav.objects.filter(pk=instance.id).first()
        children = obj.menu_set.all()
        ret = super().to_representation(instance)
        if children:
            children_list = []
            for child in children:
                children_list.append({
                    'id': child.id,
                    'title': child.title,
                    'link': child.link
                })
            ret['children'] = children_list
        if obj.position == 1:
            ret = {'product': ret}
        if obj.position == 2:
            ret = {'support': ret}
        if obj.position == 3:
            ret = {'about': ret}
        return ret


# class MenuModelSerializer(serializers.ModelSerializer):
#     """二级菜单的序列化器"""
#     class Meta:
#         model = Menu
#         fields = ["title", "link"]
#
#
# class NavModelSerializer(serializers.ModelSerializer):
#     children = MenuModelSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Nav
#         fields = ["id", "title", "link", "children", "is_site"]
class MainBannerModelSerializer(serializers.ModelSerializer):
    """横幅广告序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = MainBanner
        fields = ["title", "link", "image_url", "position"]


class CenterBannerModelSerializer(serializers.ModelSerializer):
    """横幅广告序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = MainBanner
        fields = ["title", "link", "image_url", "position"]


class MessageModelSerializer(serializers.ModelSerializer):
    """留言板序列化器"""
    # 留言板序列化器字段声明
    class Meta:
        model = Message
        fields = ["name", "email", "msg"]
