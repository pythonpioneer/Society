# Generated by Django 4.1.5 on 2023-01-23 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auths', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='password',
        ),
    ]
