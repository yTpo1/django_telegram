# Generated by Django 2.1.5 on 2019-01-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('telegram_url', models.CharField(max_length=200)),
                ('subscribers', models.IntegerField()),
            ],
        ),
    ]
