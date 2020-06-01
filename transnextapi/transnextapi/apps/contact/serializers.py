from rest_framework import serializers
from .models import Faq, Profile, Certifications, Contactus, Culture, Factory, Blog


class FaqModelSerializer(serializers.ModelSerializer):
    """FAQ的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Faq
        fields = ["context"]


class ProfileModelSerializer(serializers.ModelSerializer):
    """Company Profile的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Profile
        fields = ["context"]


class CertificationsModelSerializer(serializers.ModelSerializer):
    """Certifications的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Certifications
        fields = ["context"]


class ContactusModelSerializer(serializers.ModelSerializer):
    """Contactus的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Contactus
        fields = ["context"]


class CultureModelSerializer(serializers.ModelSerializer):
    """Company Culture的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Culture
        fields = ["context"]


class FactoryModelSerializer(serializers.ModelSerializer):
    """Factory Show的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Factory
        fields = ["context"]


class BlogModelSerializer(serializers.ModelSerializer):
    """Blog的序列化器"""
    # 模型序列化器字段声明
    class Meta:
        model = Blog
        fields = ["id", "title", "context", "img", "remark", "time"]