# Generated by Django 4.2.5 on 2023-10-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo_url',
            field=models.URLField(default=False, max_length=1000),
        ),
    ]