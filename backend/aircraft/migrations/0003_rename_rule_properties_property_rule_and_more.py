# Generated by Django 4.2.10 on 2024-02-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aircraft', '0002_alter_aircraft_properties_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='properties',
            old_name='rule',
            new_name='property_rule',
        ),
        migrations.RenameField(
            model_name='properties',
            old_name='description',
            new_name='property_value',
        ),
        migrations.RenameField(
            model_name='propertiesrule',
            old_name='name',
            new_name='rule_name',
        ),
        migrations.RemoveField(
            model_name='properties',
            name='value',
        ),
        migrations.AddField(
            model_name='properties',
            name='property_description',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='propertiesrule',
            name='rule_description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='aircraft_description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
