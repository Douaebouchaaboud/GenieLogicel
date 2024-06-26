# Generated by Django 5.0.1 on 2024-01-18 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjsServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('introduction', models.TextField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='makeup_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='makeup_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='makeup_images/')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('ville', models.CharField(default='', max_length=50)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('price_per_hour', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='ImageDjs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Djs_images/')),
                ('Djs_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.djsservices')),
            ],
        ),
        migrations.CreateModel(
            name='RatingDjs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('Djs_services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='Services.djsservices')),
            ],
        ),
    ]
