# Generated by Django 4.1.4 on 2023-01-26 11:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
