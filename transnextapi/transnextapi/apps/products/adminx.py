import xadmin
from .models import Image, Products


class ImageModelAdmin(object):
    list_display = ["title", "product", "image_url", "is_show"]


xadmin.site.register(Image, ImageModelAdmin)


class ProductsModelAdmin(object):
    list_display = ["title", "category", "general_category", "is_new", "is_show"]
    list_filter = ["category", "general_category"]


xadmin.site.register(Products, ProductsModelAdmin)
