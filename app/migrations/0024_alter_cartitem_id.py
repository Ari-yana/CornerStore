# Generated by Django 3.2.7 on 2022-04-26 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20220426_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
