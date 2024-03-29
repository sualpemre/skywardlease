# Generated by Django 4.2.10 on 2024-02-24 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0002_role_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='identity.role'),
        ),
        migrations.AlterModelTable(
            name='role',
            table='user_roles',
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
