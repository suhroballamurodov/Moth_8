# Generated by Django 4.2.6 on 2024-01-23 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha10', '0013_category_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='customer_id',
        ),
    ]
