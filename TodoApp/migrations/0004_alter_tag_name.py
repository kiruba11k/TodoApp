# Generated by Django 4.2.7 on 2023-11-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_tag_remove_task_tags_task_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default=' ', max_length=255, unique=True),
        ),
    ]