# Generated by Django 3.2.9 on 2022-10-22 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0011_delete_cloudplatform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailCodeSession',
        ),
    ]
