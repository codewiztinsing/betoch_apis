# Generated by Django 4.1.4 on 2023-01-18 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid', max_length=10)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_listing', to='listings.listing', unique=True)),
                ('realtor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realtor_orders', to='realtors.realtor')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.IntegerField(default=10000000, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('listing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='listings.listing')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='order.order')),
            ],
        ),
    ]
