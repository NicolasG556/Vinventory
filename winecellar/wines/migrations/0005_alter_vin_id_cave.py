# Generated by Django 4.2.5 on 2023-09-23 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0004_alter_vin_id_cave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vin',
            name='id_cave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wines.cavevirtuelle'),
        ),
    ]
