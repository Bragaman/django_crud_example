# Generated by Django 3.0.4 on 2020-03-22 13:47

from django.conf import settings
import django.contrib.postgres.indexes
from django.contrib.postgres.operations import BtreeGinExtension
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('subject', models.TextField(verbose_name='Subject')),
                ('text', models.TextField(verbose_name='Text')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_mail', to=settings.AUTH_USER_MODEL, verbose_name='From')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received', to=settings.AUTH_USER_MODEL, verbose_name='To')),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
                'ordering': ['-pk'],
            },
        ),
        migrations.AddIndex(
            model_name='mail',
            index=models.Index(fields=['user_from'], name='mail_mail_user_fr_d95155_idx'),
        ),
        migrations.AddIndex(
            model_name='mail',
            index=models.Index(fields=['user_to'], name='mail_mail_user_to_18bd52_idx'),
        ),
        migrations.AddIndex(
            model_name='mail',
            index=models.Index(fields=['created_at'], name='mail_mail_created_7dc6a4_idx'),
        ),
        migrations.AddIndex(
            model_name='mail',
            index=django.contrib.postgres.indexes.GinIndex(fields=['subject'], name='mail_mail_subject_1250a5_gin'),
        ),
    ]