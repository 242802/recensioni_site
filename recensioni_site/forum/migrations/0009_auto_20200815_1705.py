# Generated by Django 3.0.6 on 2020-08-15 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20200815_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sezione',
            options={'verbose_name': 'Sezione', 'verbose_name_plural': 'Sezioni'},
        ),
        migrations.AlterModelOptions(
            name='sezioneimage',
            options={},
        ),
    ]
