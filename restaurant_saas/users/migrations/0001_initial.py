# Generated by Django 3.2.18 on 2023-03-15 14:25

from django.db import migrations, models
import tenant_users.permissions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TenantUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified')),
                ('name', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, tenant_users.permissions.models.PermissionsMixinFacade),
        ),
    ]
