# Generated by Django 4.2.7 on 2024-01-12 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_song_room_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='songs',
        ),
        migrations.AddField(
            model_name='room',
            name='songs',
            field=models.ManyToManyField(null=True, to='base.song'),
        ),
    ]
