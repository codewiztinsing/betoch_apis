# Generated by Django 4.1.4 on 2023-02-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_alter_listing_sale_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='Latitude_city',
            field=models.DecimalField(decimal_places=2, default=9.005401, max_digits=5),
        ),
    ]
