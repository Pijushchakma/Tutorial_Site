# Generated by Django 3.0.9 on 2020-09-15 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_course_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.AddField(
            model_name='course',
            name='CatName',
            field=models.ForeignKey(default=90, on_delete=django.db.models.deletion.CASCADE, to='account.Category'),
            preserve_default=False,
        ),
    ]