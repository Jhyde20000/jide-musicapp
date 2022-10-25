# Generated by Django 4.1.2 on 2022-10-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyrics_song_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lyrics',
            name='song_id',
            field=models.IntegerField(),
        ),
    ]
