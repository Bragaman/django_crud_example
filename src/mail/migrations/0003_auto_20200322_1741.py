# Generated by Django 3.0.4 on 2020-03-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20200322_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
    ]
