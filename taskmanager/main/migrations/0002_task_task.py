# Generated by Django 4.1.5 on 2023-01-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task',
            field=models.TextField(default='default title', verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
