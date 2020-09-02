# Generated by Django 2.1.5 on 2019-04-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0007_channel_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='is_active',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='channel',
            name='is_featured',
            field=models.BooleanField(default='False'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='channel_images'),
        ),
    ]