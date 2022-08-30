# Generated by Django 4.0.4 on 2022-05-17 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_name_manager_manager_alter_account_expiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='manager',
            new_name='manager_name',
        ),
        migrations.AddField(
            model_name='manager',
            name='manager_email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='manager_phone',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 16, 23, 18, 34, 956431)),
        ),
    ]
