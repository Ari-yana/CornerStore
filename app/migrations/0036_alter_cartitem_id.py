# Generated by Django 3.2.7 on 2022-04-27 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_cartitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
