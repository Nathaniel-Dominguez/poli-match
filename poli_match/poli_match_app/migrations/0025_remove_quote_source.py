# Generated by Django 2.1.1 on 2018-10-10 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poli_match_app', '0024_merge_20181010_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='source',
        ),
    ]
