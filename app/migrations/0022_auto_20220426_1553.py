# Generated by Django 3.2.7 on 2022-04-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_noordersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
