# Generated by Django 5.0.2 on 2024-06-26 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.message', verbose_name='студент'),
        ),
    ]