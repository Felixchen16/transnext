# Generated by Django 3.0.5 on 2020-05-04 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200504_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(limit_choices_to={'position': 1}, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Nav', verbose_name='上级菜单'),
        ),
    ]
