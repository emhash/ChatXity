# Generated by Django 5.0.6 on 2024-07-22 17:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0004_profile_address_profile_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeCategory',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('yes_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('link', models.URLField(blank=True, max_length=500, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('seen', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice', to='app_account.noticecategory')),
                ('notice_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
