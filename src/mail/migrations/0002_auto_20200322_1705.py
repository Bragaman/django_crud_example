# Generated by Django 3.0.4 on 2020-03-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='unread',
            field=models.BooleanField(default=True, verbose_name='Is unread'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='created_at',
            field=models.DateTimeField(auto_created=True, verbose_name='Created at'),
        ),
    ]
