# Generated by Django 4.1.4 on 2023-01-26 07:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_sqrt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
