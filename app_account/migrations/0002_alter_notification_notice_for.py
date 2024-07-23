# Generated by Django 5.0.6 on 2024-07-22 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_account', '0001_initial'),
        ('app_users', '0004_profile_address_profile_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notice_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='app_users.profile'),
        ),
    ]