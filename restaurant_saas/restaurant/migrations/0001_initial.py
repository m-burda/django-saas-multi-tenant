# Generated by Django 3.2.18 on 2023-03-15 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MenuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='<django.db.models.fields.related.ForeignKey> Menu', max_length=20)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenant.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.categorymodel')),
            ],
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.menumodel'),
        ),
    ]
