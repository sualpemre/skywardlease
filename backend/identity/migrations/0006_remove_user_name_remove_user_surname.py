# Generated by Django 4.2.10 on 2024-02-25 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0005_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
    ]
