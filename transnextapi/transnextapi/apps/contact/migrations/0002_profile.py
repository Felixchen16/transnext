# Generated by Django 3.0.5 on 2020-05-27 09:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Company Profile内容')),
            ],
            options={
                'verbose_name': 'Company Profile',
                'verbose_name_plural': 'Company Profile',
                'db_table': 'tn_profile',
            },
        ),
    ]