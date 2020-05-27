from uuid import uuid4
from django.db import models
from transnextapi.apps.home import models as home
from transnextapi.utils.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
def make_file_path(instance, filename):
    upload_to = 'products'
    p_name = instance.product.title
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    path = f'{upload_to}/{p_name}/{filename}'
    return path


class Image(BaseModel):
    title = models.CharField(max_length=500, verbose_name="图片标题")
    image_url = models.ImageField(upload_to=make_file_path,
                                  null=True, blank=True,
                                  max_length=255,
                                  verbose_name="图片地址", )
    product = models.ForeignKey('Products', related_name='image_url', verbose_name="所属产品", on_delete=models.DO_NOTHING)

    # 表信息声明
    class Meta:
        db_table = "tn_image"
        verbose_name = "产品图片"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title


class Products(BaseModel):
    title = models.CharField(max_length=500, verbose_name="产品标题")
    specs = RichTextUploadingField(null=True, blank=True, verbose_name="产品规格")
    context = RichTextUploadingField(null=True, blank=True, verbose_name="产品详情")
    is_new = models.BooleanField(default=False, verbose_name="是否推新")
    general_category = models.ForeignKey('home.Nav',
                                         verbose_name="所属大类",
                                         on_delete=models.DO_NOTHING,
                                         limit_choices_to={'position': 1})
    category = models.ForeignKey('home.Menu', verbose_name="所属分类", on_delete=models.DO_NOTHING)

    # 表信息声明
    class Meta:
        db_table = "tn_products"
        verbose_name = "产品管理"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title
