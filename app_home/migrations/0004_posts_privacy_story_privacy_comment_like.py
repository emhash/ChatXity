# Generated by Django 5.0.6 on 2024-06-19 06:04

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0003_remove_posts_image_postimage'),
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='privacy',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends Only'), ('only_me', 'Only Me')], default='public', max_length=50),
        ),
        migrations.AddField(
            model_name='story',
            name='privacy',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends Only'), ('only_me', 'Only Me')], default='public', max_length=50),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='app_home.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_home.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='app_home.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.profile')),
            ],
            options={
                'unique_together': {('post', 'user')},
            },
        ),
    ]