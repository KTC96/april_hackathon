# Generated by Django 4.2 on 2024-04-23 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parent_post',
        ),
    ]
