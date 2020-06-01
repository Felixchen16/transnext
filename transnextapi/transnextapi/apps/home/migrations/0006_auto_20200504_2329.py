# Generated by Django 3.0.5 on 2020-05-04 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200504_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': '二级菜单', 'verbose_name_plural': '二级菜单'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(limit_choices_to={'nav__position': 1}, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Nav', verbose_name='上级菜单'),
        ),
        migrations.AlterModelTable(
            name='menu',
            table='tn_menu',
        ),
    ]