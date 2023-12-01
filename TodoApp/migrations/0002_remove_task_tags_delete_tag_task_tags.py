# Generated by Django 4.2.7 on 2023-11-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]