# Generated by Django 3.0.9 on 2020-09-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_allcourses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('Math', 'Math'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology')], default=2, max_length=20),
            preserve_default=False,
        ),
    ]
