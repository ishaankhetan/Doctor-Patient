# Generated by Django 2.2.4 on 2020-03-13 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0016_auto_20200313_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='postgrad',
            field=models.CharField(choices=[('MD', 'MD'), ('MS', 'MS'), ('Diploma', 'Diploma')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(choices=[('DM', 'DM'), ('MCh', 'MCh')], default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DOB',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 13, 51, 2, 530049), null=True),
        ),
    ]
