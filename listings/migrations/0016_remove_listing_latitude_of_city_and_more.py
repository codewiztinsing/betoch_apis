# Generated by Django 4.1.4 on 2023-03-01 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_alter_listing_latitude_of_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='Latitude_of_city',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='Longitude_of_city',
        ),
    ]
