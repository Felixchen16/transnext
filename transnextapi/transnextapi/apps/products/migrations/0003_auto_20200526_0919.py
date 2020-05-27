# Generated by Django 3.0.5 on 2020-05-26 01:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200526_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='context',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='产品详情'),
        ),
        migrations.AlterField(
            model_name='products',
            name='specs',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='产品规格'),
        ),
    ]
