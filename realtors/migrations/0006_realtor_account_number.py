# Generated by Django 4.1.4 on 2023-03-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0005_alter_realtor_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='Account_number',
            field=models.IntegerField(null=True),
        ),
    ]
