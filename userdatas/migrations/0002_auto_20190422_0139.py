# Generated by Django 2.1.2 on 2019-04-22 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdatas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='userid',
            field=models.IntegerField(max_length=200),
        ),
    ]