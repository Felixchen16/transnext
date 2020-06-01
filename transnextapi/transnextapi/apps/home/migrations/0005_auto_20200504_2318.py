# Generated by Django 3.0.5 on 2020-05-04 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200426_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nav',
            name='parent',
        ),
        migrations.AlterField(
            model_name='nav',
            name='link',
            field=models.CharField(max_length=500, verbose_name='菜单链接'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='position',
            field=models.IntegerField(choices=[(1, 'Products'), (2, 'Support'), (3, 'About')], default=1, verbose_name='菜单所属位置'),
        ),
        migrations.AlterField(
            model_name='nav',
            name='title',
            field=models.CharField(max_length=500, verbose_name='菜单标题'),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('order', models.IntegerField(default=1, verbose_name='排序')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('title', models.CharField(max_length=500, verbose_name='菜单标题')),
                ('link', models.CharField(max_length=500, verbose_name='菜单链接')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.Nav', verbose_name='上级菜单')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]