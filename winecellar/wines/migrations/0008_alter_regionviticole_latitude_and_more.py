# Generated by Django 4.2.5 on 2023-10-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0007_regionviticole_latitude_regionviticole_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionviticole',
            name='latitude',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='regionviticole',
            name='longitude',
            field=models.FloatField(default=1.0),
        ),
    ]
