# Generated by Django 2.2.10 on 2020-05-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0002_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
    ]