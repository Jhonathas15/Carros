# Generated by Django 5.0.7 on 2024-08-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_carinventory_alter_car_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
