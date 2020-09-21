# Generated by Django 3.0.9 on 2020-09-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20200915_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='course',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='status',
            field=models.CharField(default='Not Started', max_length=20),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='AllCourses',
        ),
    ]
