# Generated by Django 3.2.9 on 2021-11-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0008_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='rate',
            field=models.IntegerField(default=1),
        ),
    ]
