# Generated by Django 4.2.13 on 2024-07-13 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("minibar", "0002_alter_product_price_alter_room_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="date",
            field=models.DateTimeField(),
        ),
    ]
