# Generated by Django 2.1.2 on 2019-04-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdatas', '0002_auto_20190422_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='userid',
            field=models.IntegerField(),
        ),
    ]