from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Faq(models.Model):
    context = RichTextUploadingField(null=True, blank=True, verbose_name="FAQ内容")

    # 表信息声明
    class Meta:
        db_table = "tn_faq"
        verbose_name = "FAQ"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return str(self.pk)


class Profile(models.Model):
    context = RichTextUploadingField(null=True, blank=True, verbose_name="Company Profile内容")

    # 表信息声明
    class Meta:
        db_table = "tn_profile"
        verbose_name = "Company Profile"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return str(self.pk)


class Culture(models.Model):
    context = RichTextUploadingField(null=True, blank=True, verbose_name="Company Culture内容")

    # 表信息声明
    class Meta:
        db_table = "tn_culture"
        verbose_name = "Company Culture"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return str(self.pk)


class Factory(models.Model):
    context = RichTextUploadingField(null=True, blank=True, verbose_name="Factory Show内容")

    # 表信息声明
    class Meta:
        db_table = "tn_factory"
        verbose_name = "Factory Show"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return str(self.pk)


class Certifications(models.Model):
    context = RichTextUploadingField(null=True, blank=True, verbose_name="Certifications内容")

    # 表信息声明
    class Meta:
        db_table = "tn_certifications"
        verbose_name = "Certifications"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return str(self.pk)


class Contactus(models.Model):
    context = RichTextUploadingField(null=True, blank=True, verbose_name="Contact Us内容")

    # 表信息声明
    class Meta:
        db_table = "tn_contactus"
        verbose_name = "Contact Us"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return str(self.pk)


class Blog(models.Model):
    title = models.CharField(max_length=500, verbose_name="Blog标题")
    context = RichTextUploadingField(null=True, blank=True, verbose_name="Blog内容")
    img = models.ImageField(upload_to='blog',
                            null=True, blank=True,
                            max_length=255,
                            verbose_name="图片地址", )
    remark = models.TextField(null=True, blank=True, verbose_name="备注")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    # 表信息声明
    class Meta:
        db_table = "tn_blog"
        verbose_name = "Blog"
        verbose_name_plural = verbose_name

    # 自定义方法
    def __str__(self):
        return self.title
