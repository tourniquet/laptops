# Generated by Django 4.1.3 on 2022-11-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0007_remove_laptop_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
