# Generated by Django 4.2.6 on 2024-01-23 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loyiha10', '0010_rename_category_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loyiha10.category'),
            preserve_default=False,
        ),
    ]