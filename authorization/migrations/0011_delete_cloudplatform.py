# Generated by Django 3.2.9 on 2022-10-20 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0010_alter_emailcodesession_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CloudPlatform',
        ),
    ]
