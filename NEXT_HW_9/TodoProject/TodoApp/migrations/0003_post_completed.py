# Generated by Django 5.0.4 on 2024-04-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_post_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
