# Generated by Django 4.1 on 2022-08-24 04:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcentro', '0003_rename_nacionalidadd_nacionalidad_nacionalidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumnos',
            options={'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AlterModelOptions(
            name='alumnospormodulos',
            options={'verbose_name_plural': 'Alumnos por Modulos'},
        ),
        migrations.AlterModelOptions(
            name='cursos',
            options={'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterModelOptions(
            name='modulos',
            options={'verbose_name_plural': 'Modulos'},
        ),
        migrations.AlterModelOptions(
            name='nacionalidad',
            options={'verbose_name_plural': 'Nacionalidades'},
        ),
        migrations.AlterModelOptions(
            name='nomenclador',
            options={'verbose_name_plural': 'Nomencladores'},
        ),
        migrations.RemoveField(
            model_name='alumnos',
            name='Sexo',
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Telefono',
            field=models.BigIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]