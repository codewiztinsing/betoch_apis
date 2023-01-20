# Generated by Django 4.1.4 on 2023-01-18 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=144, max_digits=6)),
                ('published', models.BooleanField(default=False)),
                ('sale_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For rent', 'For Rent')], default='For Sale', max_length=10)),
                ('bed_rooms', models.IntegerField()),
                ('bath_rooms', models.IntegerField(default=0)),
                ('sqrt', models.DecimalField(decimal_places=2, max_digits=4)),
                ('home_type', models.CharField(choices=[('Apartama', 'Apartama'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse')], default='Condo', max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('avgRating', models.IntegerField(default=1)),
                ('ratings', models.IntegerField(default=1)),
                ('oldPrice', models.DecimalField(decimal_places=2, default=144, max_digits=6)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('image_1', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('image_2', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('image_3', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('image_4', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('image_5', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realtors', to='realtors.realtor')),
            ],
            options={
                'verbose_name_plural': 'Listings',
                'ordering': ('-date_added',),
            },
        ),
    ]
