# Generated by Django 3.2.7 on 2022-04-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_sidemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
    ]
