# Generated by Django 2.1.1 on 2018-10-09 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poli_match_app', '0010_auto_20181009_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='next_election',
            field=models.IntegerField(default=0),
        ),
    ]
