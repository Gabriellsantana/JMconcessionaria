# Generated by Django 4.2.6 on 2023-11-03 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appConcessionaria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
    ]
