# Generated by Django 4.1.7 on 2023-04-03 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0002_food_description_food_special_price_and_more'),
        ('app_general', '0005_remove_subsciption_food_subsciption_food_set'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subsciption',
            new_name='Subscription',
        ),
    ]