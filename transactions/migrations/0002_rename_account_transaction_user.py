# Generated by Django 5.0.1 on 2024-03-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='account',
            new_name='user',
        ),
    ]
