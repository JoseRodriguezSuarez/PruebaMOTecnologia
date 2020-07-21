# Generated by Django 3.0.8 on 2020-07-20 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadenaEvolucion', '0003_pokemon_cadevolutiva'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Estadisticas',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='attack',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='special_attack',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='special_defense',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemon',
            name='speed',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
