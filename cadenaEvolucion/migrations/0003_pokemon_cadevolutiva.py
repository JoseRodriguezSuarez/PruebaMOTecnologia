# Generated by Django 3.0.8 on 2020-07-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadenaEvolucion', '0002_remove_pokemon_evolucion'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='cadEvolutiva',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]