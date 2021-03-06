# Generated by Django 2.0.6 on 2018-10-25 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saver',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('is_free', models.IntegerField(default=0)),
                ('next_destination', models.CharField(max_length=100)),
                ('saver_no', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('lat', models.CharField(max_length=100)),
                ('lng', models.CharField(max_length=100)),
                ('no_of_person', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_severe_person', models.IntegerField(default=0)),
                ('req_no', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
