# Generated by Django 2.0.6 on 2018-10-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_response', '0003_auto_20181025_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saver',
            name='next_destination',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
