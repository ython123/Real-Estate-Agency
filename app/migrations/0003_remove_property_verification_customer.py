# Generated by Django 4.0.8 on 2022-12-04 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_property_apply1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_verification',
            name='customer',
        ),
    ]
