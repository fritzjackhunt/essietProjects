# Generated by Django 3.0.7 on 2021-04-25 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210424_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='message',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='your_name',
        ),
    ]