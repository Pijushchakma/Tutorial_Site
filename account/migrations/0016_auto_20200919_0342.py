# Generated by Django 3.0.9 on 2020-09-19 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20200918_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='now',
            field=models.IntegerField(default=0),
        ),
    ]