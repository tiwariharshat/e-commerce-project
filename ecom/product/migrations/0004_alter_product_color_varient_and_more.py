# Generated by Django 4.1.1 on 2022-10-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_colorvariant_sizevariant_product_color_varient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color_varient',
            field=models.ManyToManyField(blank=True, null=True, to='product.colorvariant'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, null=True, to='product.sizevariant'),
        ),
    ]
