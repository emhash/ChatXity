# Generated by Django 5.0.6 on 2024-07-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0010_remove_postimage_own_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='privacy',
            field=models.CharField(choices=[('public', 'Public'), ('friends', 'Friends Only'), ('only_me', 'Only Me')], default='public', max_length=50),
        ),
    ]
