# Generated by Django 4.1 on 2023-12-08 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0010_rename_categoryname_product_namecategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='namecategory',
        ),
    ]
