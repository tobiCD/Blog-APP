# Generated by Django 4.2.7 on 2024-01-12 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_room_songs_room_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='songs',
        ),
        migrations.AddField(
            model_name='room',
            name='songs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.song'),
        ),
    ]
