# Generated by Django 4.0.2 on 2022-02-01 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dronecategory',
            options={'ordering': ('name',), 'verbose_name_plural': 'Drone_categories'},
        ),
    ]