# Generated by Django 3.2.9 on 2021-11-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0009_ingredients_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='CP',
            field=models.IntegerField(default=0),
        ),
    ]
