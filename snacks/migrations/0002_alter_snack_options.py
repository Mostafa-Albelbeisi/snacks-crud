# Generated by Django 4.1.3 on 2022-12-05 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snack',
            options={'ordering': ['-pk'], 'verbose_name_plural': 'my things'},
        ),
    ]
