# Generated by Django 3.0.5 on 2020-05-27 10:57

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_certifications_contactus_culture_factory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Blog标题')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Blog内容')),
                ('img', models.ImageField(blank=True, max_length=255, null=True, upload_to='blog', verbose_name='图片地址')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blog',
                'db_table': 'tn_blog',
            },
        ),
    ]
