# Generated by Django 3.0.8 on 2020-07-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estadisticas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cuant', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nPok', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('evolucion', models.CharField(max_length=100)),
            ],
        ),
    ]
