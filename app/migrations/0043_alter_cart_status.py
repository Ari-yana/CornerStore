# Generated by Django 3.2.7 on 2022-04-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='unpaid', max_length=1000, null=True),
        ),
    ]
