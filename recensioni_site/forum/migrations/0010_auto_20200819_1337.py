# Generated by Django 3.0.6 on 2020-08-19 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20200815_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sezione',
            name='descrizione',
            field=models.TextField(),
        ),
    ]
