# Generated by Django 4.1.4 on 2023-01-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorites', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='realtor',
        ),
        migrations.AddField(
            model_name='favorite',
            name='realtor_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
