# Generated by Django 2.2.4 on 2021-01-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_manage_app', '0003_auto_20210128_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
