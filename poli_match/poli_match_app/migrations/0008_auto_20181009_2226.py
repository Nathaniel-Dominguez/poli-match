# Generated by Django 2.1.1 on 2018-10-09 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poli_match_app', '0007_auto_20181009_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='missed_votes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='politician',
            name='total_votes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='politician',
            name='votes_with_party_pct',
            field=models.IntegerField(),
        ),
    ]
