# Generated by Django 5.0.1 on 2024-03-06 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_borrow_user'),
        ('reglogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reglogin.useraccount'),
        ),
    ]
