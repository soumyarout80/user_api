# Generated by Django 4.0.4 on 2022-05-17 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_manager_manager_manager_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountDetails',
            new_name='AccountDetail',
        ),
        migrations.AlterField(
            model_name='account',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 23, 57, 24, 955292)),
        ),
    ]