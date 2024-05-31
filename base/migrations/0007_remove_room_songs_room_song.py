# Generated by Django 4.2.7 on 2024-01-09 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_room_song_room_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='songs',
        ),
        migrations.AddField(
            model_name='room',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.song'),
        ),
    ]
