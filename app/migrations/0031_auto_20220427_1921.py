# Generated by Django 3.2.7 on 2022-04-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20220427_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='side1',
            field=models.CharField(choices=[('--Choose a Side--', (('corn nuggets', 'Corn Nuggets'), ('tater tots', 'Tater Tots'), ('french fries', 'French Fries'), ('onion rings', 'Onion Rings'), ('fried okra', 'Fried Okra'), ('loaded baked potato', 'Loaded Baked Potato'), ('side salad', 'Side Salad')))], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='side2',
            field=models.CharField(choices=[('--Choose a Side--', (('corn nuggets', 'Corn Nuggets'), ('tater tots', 'Tater Tots'), ('french fries', 'French Fries'), ('onion rings', 'Onion Rings'), ('fried okra', 'Fried Okra'), ('loaded baked potato', 'Loaded Baked Potato'), ('side salad', 'Side Salad')))], max_length=20, null=True),
        ),
    ]
