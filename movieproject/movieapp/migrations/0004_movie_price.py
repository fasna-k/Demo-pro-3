# Generated by Django 4.2.3 on 2023-07-12 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_movie_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='price',
            field=models.IntegerField(default=4568),
            preserve_default=False,
        ),
    ]
