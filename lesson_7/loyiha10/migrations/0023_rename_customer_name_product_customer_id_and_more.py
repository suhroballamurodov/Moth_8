# Generated by Django 4.2.6 on 2024-01-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha10', '0022_alter_product_create_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='customer_name',
            new_name='customer_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='create_time',
        ),
        migrations.AddField(
            model_name='product',
            name='data',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
