from rest_framework import serializers
from .models import Image, Products


class ImageModelSerializer(serializers.ModelSerializer):
    """产品图片的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Image
        fields = ["title", "image_url"]


class ProductsModelSerializer(serializers.ModelSerializer):
    """产品的序列化器"""
    image_url = ImageModelSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='title')
    general_category = serializers.SlugRelatedField(read_only=True, slug_field='title')

    # 模型序列化器字段声明
    class Meta:
        model = Products
        fields = ["id", "title", "specs", "context", "image_url", "is_new", "category", "general_category"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['breadcrumb'] = {
            'title': instance.general_category.title,
            'path_one': '/categroy/' + str(instance.general_category.id) + instance.general_category.link,
            'path_two': '/products/' + str(instance.category.id) + instance.category.link
        }
        return ret
