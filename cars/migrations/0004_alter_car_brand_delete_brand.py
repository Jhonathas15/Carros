# Generated by Django 5.0.7 on 2024-07-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_brand_alter_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
