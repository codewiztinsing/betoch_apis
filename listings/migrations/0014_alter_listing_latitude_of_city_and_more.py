# Generated by Django 4.1.4 on 2023-03-01 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_rename_latitude_city_listing_latitude_of_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Latitude_of_city',
            field=models.DecimalField(decimal_places=2, default=9.005401, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Longitude_of_city',
            field=models.DecimalField(decimal_places=2, default=38.763611, max_digits=5, null=True),
        ),
    ]
