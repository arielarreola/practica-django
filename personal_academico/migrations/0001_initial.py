# Generated by Django 5.1.3 on 2024-11-26 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('carrera', models.CharField(choices=[('CIB', 'Ingenieria Cibernetica'), ('PSI', 'Psicologia'), ('NUT', 'Nutricion'), ('DER', 'Derecho'), ('EDI', 'Educación')], max_length=255)),
                ('semestre', models.IntegerField()),
            ],
        ),
    ]
