# Generated by Django 4.0.1 on 2023-09-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0002_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
