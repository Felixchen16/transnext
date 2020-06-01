# Generated by Django 3.0.5 on 2020-05-27 09:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Certifications内容')),
            ],
            options={
                'verbose_name': 'Certifications',
                'verbose_name_plural': 'Certifications',
                'db_table': 'tn_certifications',
            },
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Contact Us内容')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
                'db_table': 'tn_contactus',
            },
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Company Culture内容')),
            ],
            options={
                'verbose_name': 'Company Culture',
                'verbose_name_plural': 'Company Culture',
                'db_table': 'tn_culture',
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Factory Show内容')),
            ],
            options={
                'verbose_name': 'Factory Show',
                'verbose_name_plural': 'Factory Show',
                'db_table': 'tn_factory',
            },
        ),
    ]