from django.db import models
from transnextapi.utils.models import BaseModel


# Create your models here.
class Banner(BaseModel):
    """轮播图模型"""
    # 模型字段
    title = models.CharField(max_length=500, verbose_name="广告标题")
    link = models.CharField(max_length=500, verbose_name="广告链接")
    image_url = models.ImageField(upload_to="banner",
                                  null=True, blank=True,
                                  max_length=255,
                                  verbose_name="图片地址",)
    remark = models.TextField(verbose_name="备注信息")

    # 表信息声明
    class Meta:
        db_table = "tn_banner"
        verbose_name = "轮播广告"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title


class Nav(BaseModel):
    """导航菜单模型"""
    POSITION_OPTION = (
        (1, "Products"),
        (2, "Support"),
        (3, "About"),
    )
    title = models.CharField(max_length=500, verbose_name="菜单标题")
    link = models.CharField(max_length=500, verbose_name="菜单链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name="菜单所属位置")
    is_site = models.BooleanField(default=False, verbose_name="是否是站外地址")

    # 表信息声明
    class Meta:
        db_table = "tn_nav"
        verbose_name = "导航菜单"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title


class Menu(BaseModel):
    """二级菜单栏模型"""
    title = models.CharField(max_length=500, verbose_name="菜单标题")
    link = models.CharField(max_length=500, verbose_name="菜单链接")
    parent = models.ForeignKey('Nav',
                               verbose_name="上级菜单",
                               on_delete=models.DO_NOTHING,
                               limit_choices_to={'position': 1})

    # 表信息声明
    class Meta:
        db_table = "tn_menu"
        verbose_name = "二级菜单"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title


class MainBanner(BaseModel):
    """横幅广告模型"""
    POSITION_OPTION = (
        (1, "上面的横幅"),
        (2, "下面的横幅")
    )
    title = models.CharField(max_length=500, verbose_name="横幅标题")
    link = models.CharField(max_length=500, verbose_name="横幅链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name="横幅所属位置")
    image_url = models.ImageField(upload_to="main_banner",
                                  null=True, blank=True,
                                  max_length=255,
                                  verbose_name="横幅图片",)

    # 表信息声明
    class Meta:
        db_table = "tn_main_banner"
        verbose_name = "横幅广告"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title


class CenterBanner(BaseModel):
    """中间广告模型"""
    POSITION_OPTION = (
        (1, "第一列大图"),
        (2, "第一列小图"),
        (3, "第二列小图"),
        (4, "第二列大图")
    )
    title = models.CharField(max_length=500, verbose_name="广告标题")
    link = models.CharField(max_length=500, verbose_name="广告链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name="广告所属位置")
    image_url = models.ImageField(upload_to="center_banner",
                                  null=True, blank=True,
                                  max_length=255,
                                  verbose_name="横幅图片",)

    # 表信息声明
    class Meta:
        db_table = "tn_center_banner"
        verbose_name = "中间广告"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=500, verbose_name="客户姓名")
    email = models.CharField(max_length=500, verbose_name="客户邮箱")
    msg = models.TextField(verbose_name="客户留言")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    # 表信息声明
    class Meta:
        db_table = "tn_message"
        verbose_name = "留言板"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.name
