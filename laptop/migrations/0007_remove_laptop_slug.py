# Generated by Django 4.1.3 on 2022-11-29 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0006_laptop_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='slug',
        ),
    ]