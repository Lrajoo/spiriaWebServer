# Generated by Django 2.1.2 on 2019-04-22 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdatas', '0003_auto_20190422_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='userid',
            field=models.CharField(max_length=100),
        ),
    ]
