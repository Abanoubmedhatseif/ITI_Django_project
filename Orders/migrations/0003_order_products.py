# Generated by Django 4.0.10 on 2024-04-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_category'),
        ('Orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='Product.product'),
        ),
    ]