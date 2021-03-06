# Generated by Django 3.0.5 on 2020-05-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200510_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='CenterBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('order', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=500, verbose_name='广告标题')),
                ('link', models.CharField(max_length=500, verbose_name='广告链接')),
                ('position', models.IntegerField(choices=[(1, '第一列大图'), (2, '第一列小图'), (3, '第二列小图'), (4, '第二列大图')], default=1, verbose_name='广告所属位置')),
                ('image_url', models.ImageField(blank=True, max_length=255, null=True, upload_to='center_banner', verbose_name='横幅图片')),
            ],
            options={
                'verbose_name': '中间广告',
                'verbose_name_plural': '中间广告',
                'db_table': 'tn_center_banner',
            },
        ),
    ]
