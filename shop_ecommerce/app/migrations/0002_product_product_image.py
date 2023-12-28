# Generated by Django 4.2.7 on 2023-11-13 05:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='productimg'),
            preserve_default=False,
        ),
    ]
