# Generated by Django 4.1 on 2023-12-08 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0006_product_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='diff',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
