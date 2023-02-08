# Generated by Django 4.1.4 on 2023-01-30 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0002_alter_realtor_email'),
        ('listings', '0007_alter_listing_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
                ('realtor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='realtors.realtor')),
            ],
        ),
    ]
