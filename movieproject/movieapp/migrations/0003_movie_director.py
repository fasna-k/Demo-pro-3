# Generated by Django 4.2.3 on 2023-07-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='sgh', max_length=100),
            preserve_default=False,
        ),
    ]
