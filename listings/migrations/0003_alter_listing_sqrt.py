# Generated by Django 4.1.4 on 2023-01-20 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_listing_realtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='sqrt',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=4),
        ),
    ]