# Generated by Django 3.2 on 2023-06-02 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True, default='none'),
            preserve_default=False,
        ),
    ]
