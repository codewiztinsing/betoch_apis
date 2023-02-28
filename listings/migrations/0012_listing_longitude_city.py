# Generated by Django 4.1.4 on 2023-02-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_listing_latitude_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Longitude_city',
            field=models.DecimalField(decimal_places=2, default=38.763611, max_digits=5),
        ),
    ]