# Generated by Django 5.1.3 on 2024-11-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_academico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ocupacion', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=80)),
                ('no_materias', models.IntegerField()),
            ],
        ),
    ]
