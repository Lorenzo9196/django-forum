# Generated by Django 4.2.1 on 2023-06-06 04:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_topic_room_user_message_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='handle',
        ),
        migrations.AddField(
            model_name='message',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]