# Generated by Django 2.1.5 on 2019-04-19 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0005_auto_20190419_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='category_images'),
        ),
    ]