# Generated by Django 3.2.9 on 2022-10-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_auto_20221009_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcodesession',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]