# Generated by Django 3.2.18 on 2023-03-17 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
        ('restaurant', '0002_auto_20230316_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant'),
        ),
    ]