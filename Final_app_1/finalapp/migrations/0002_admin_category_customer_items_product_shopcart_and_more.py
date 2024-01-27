# Generated by Django 5.0.1 on 2024-01-24 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Ismi')),
                ('status', models.CharField(choices=[('admin', 'Admin'), ('creater', 'Creater')], default='admin', max_length=10, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Maxsulot kategoriyasi')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=30, verbose_name='Ism')),
                ('l_name', models.CharField(max_length=30, verbose_name='Familiya')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Yoshi')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.TextField(verbose_name='Maxsulot haqida')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='Maxsulot nomi')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Ishlab chiqarilgan vaqti')),
                ('delete_day', models.IntegerField(verbose_name='Yaroqlilik muddati')),
                ('price', models.IntegerField(verbose_name='Narhi')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.category', verbose_name='Category')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.customer')),
                ('items_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.items', verbose_name='Items')),
            ],
        ),
        migrations.CreateModel(
            name='Shopcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Maxsulot narxi')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Karta hisobi')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.customer', verbose_name='Customer Id')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finalapp.product')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
