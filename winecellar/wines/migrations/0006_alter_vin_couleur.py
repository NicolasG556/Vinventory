# Generated by Django 4.2.5 on 2023-09-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0005_alter_vin_id_cave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vin',
            name='couleur',
            field=models.CharField(choices=[('ROUGE', 'Rouge'), ('BLANC', 'Blanc'), ('ROSÉ', 'Rose')], max_length=6),
        ),
    ]