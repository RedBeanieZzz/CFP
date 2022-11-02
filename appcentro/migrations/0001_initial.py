# Generated by Django 4.1 on 2022-08-19 02:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('Documento', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999999)])),
                ('ApellidoyNombre', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=30)),
                ('Localidad', models.CharField(max_length=25)),
                ('Telefono', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999999)])),
                ('Estudios', models.CharField(max_length=15)),
                ('Nacimiento', models.DateTimeField()),
                ('LugarDeNacimiento', models.CharField(max_length=30)),
                ('ProvinciaDeNacimiento', models.CharField(max_length=20)),
                ('Sexo', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('IDCurso', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999)])),
                ('CFP', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('CicloLectivo', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('Nombre', models.CharField(max_length=80)),
                ('Resolucion', models.CharField(max_length=20)),
                ('Anexo', models.CharField(max_length=5)),
                ('CantidadDeClases', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('Inicio', models.DateTimeField()),
                ('Final', models.DateField()),
                ('Horario', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('IDNacionalidad', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999)])),
                ('Nacionalidadd', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Nomenclador',
            fields=[
                ('CodigoDeArea', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('CodigoDePerfil', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('NombreDeArea', models.CharField(max_length=30)),
                ('NombreDePerfil', models.CharField(max_length=80)),
                ('CargaHoraria', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('Requisitos', models.CharField(max_length=30)),
                ('NivelDeCertificacion', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9)])),
                ('Programacion', models.CharField(max_length=25)),
                ('TipoDeCapacitacion', models.CharField(max_length=4)),
                ('Anexo', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('Observaciones', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modulos',
            fields=[
                ('IDModulo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('IDCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcentro.cursos')),
            ],
        ),
        migrations.AddField(
            model_name='cursos',
            name='CodigoDeArea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appcentro.Nomenclador.CodigoDeArea+', to='appcentro.nomenclador'),
        ),
        migrations.AddField(
            model_name='cursos',
            name='CodigoDePerfil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appcentro.Nomenclador.CodigoDePerfil+', to='appcentro.nomenclador'),
        ),
        migrations.CreateModel(
            name='AlumnosPorModulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nota', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('Vencimiento', models.DateTimeField()),
                ('CFP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appcentro.Cursos.CFP+', to='appcentro.cursos')),
                ('Documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcentro.alumnos')),
                ('IDCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appcentro.Cursos.IDCurso+', to='appcentro.cursos')),
                ('IDModulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcentro.modulos')),
            ],
        ),
        migrations.AddField(
            model_name='alumnos',
            name='IDNacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcentro.nacionalidad'),
        ),
    ]
