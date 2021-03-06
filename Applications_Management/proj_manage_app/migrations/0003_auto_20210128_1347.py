# Generated by Django 2.2.4 on 2021-01-28 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj_manage_app', '0002_auto_20210127_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_archived',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_tasks', to='proj_manage_app.Project'),
        ),
    ]
