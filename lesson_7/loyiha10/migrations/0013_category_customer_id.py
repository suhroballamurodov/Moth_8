# Generated by Django 4.2.6 on 2024-01-23 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha10', '0012_remove_customer_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='customer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loyiha10.customer'),
            preserve_default=False,
        ),
    ]
