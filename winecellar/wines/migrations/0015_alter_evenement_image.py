# Generated by Django 4.2.5 on 2023-10-18 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0014_alter_evenement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evenement',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wines.photo'),
        ),
    ]
