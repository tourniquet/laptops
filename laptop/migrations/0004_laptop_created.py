# Generated by Django 4.1.2 on 2022-11-22 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laptop', '0003_laptop_title_alter_laptop_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
