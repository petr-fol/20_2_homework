# Generated by Django 5.0.2 on 2024-06-23 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_version'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Version',
            new_name='ProductVersion',
        ),
    ]