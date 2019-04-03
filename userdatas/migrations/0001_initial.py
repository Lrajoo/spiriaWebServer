# Generated by Django 2.1.2 on 2019-04-01 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('spiral', models.ImageField(upload_to='images')),
                ('tremor', models.IntegerField()),
                ('questionnaire', models.IntegerField()),
                ('prediction', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
