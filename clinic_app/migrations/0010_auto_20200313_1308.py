# Generated by Django 2.2.4 on 2020-03-13 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0009_auto_20200313_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 13, 8, 55, 93069), null=True),
        ),
    ]
