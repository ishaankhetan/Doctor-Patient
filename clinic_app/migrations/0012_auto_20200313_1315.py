# Generated by Django 2.2.4 on 2020-03-13 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0011_auto_20200313_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 13, 15, 46, 810630), null=True),
        ),
    ]
