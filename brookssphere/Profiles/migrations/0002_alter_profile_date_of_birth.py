# Generated by Django 4.2 on 2023-05-04 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 4, 15, 56, 0, 182827)),
        ),
    ]
