# Generated by Django 5.0.6 on 2024-06-26 02:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='candidates',
            field=models.ManyToManyField(to='main_app.record'),
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
