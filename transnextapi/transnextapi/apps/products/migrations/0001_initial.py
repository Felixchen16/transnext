# Generated by Django 3.0.5 on 2020-05-25 14:16

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import transnextapi.apps.products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0012_message_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('order', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=500, verbose_name='产品标题')),
                ('specs', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='产品规格')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=2048, null=True, verbose_name='产品详情')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Menu', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '产品图片',
                'verbose_name_plural': '产品图片',
                'db_table': 'tn_products',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('order', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=500, verbose_name='图片标题')),
                ('image_url', models.ImageField(blank=True, max_length=255, null=True, upload_to=transnextapi.apps.products.models.make_file_path, verbose_name='图片地址')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Products', verbose_name='所属产品')),
            ],
            options={
                'verbose_name': '产品图片',
                'verbose_name_plural': '产品图片',
                'db_table': 'tn_image',
            },
        ),
    ]
