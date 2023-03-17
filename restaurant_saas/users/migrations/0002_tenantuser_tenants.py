# Generated by Django 3.2.18 on 2023-03-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenantuser',
            name='tenants',
            field=models.ManyToManyField(blank=True, help_text='The tenants this user belongs to.', related_name='user_set', to='tenant.Tenant', verbose_name='tenants'),
        ),
    ]