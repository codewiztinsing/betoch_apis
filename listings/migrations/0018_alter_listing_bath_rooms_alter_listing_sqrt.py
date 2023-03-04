# Generated by Django 4.1.4 on 2023-03-03 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bath_rooms',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqrt',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=10),
        ),
    ]
