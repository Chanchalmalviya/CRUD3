# Generated by Django 4.2.8 on 2023-12-04 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chanchal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
    ]