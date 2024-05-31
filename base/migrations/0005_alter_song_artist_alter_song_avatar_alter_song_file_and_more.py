# Generated by Django 4.2.7 on 2023-12-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_song_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='song_file/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
