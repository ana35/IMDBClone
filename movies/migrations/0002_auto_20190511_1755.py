# Generated by Django 2.2 on 2019-05-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_score',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity_99',
            field=models.FloatField(),
        ),
    ]
