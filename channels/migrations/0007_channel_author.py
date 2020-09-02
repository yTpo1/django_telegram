# Generated by Django 2.1.5 on 2019-04-25 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('channels', '0006_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='author',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]