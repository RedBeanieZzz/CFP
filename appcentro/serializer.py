from dataclasses import field, fields
from rest_framework import serializers
from .models import Alumnos, Cursos, Nacionalidad, Nomenclador, Modulos, AlumnosPorModulos


class AlumnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumnos
		fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cursos 
		fields = '__all__'

class NacionalidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nacionalidad
		fields = '__all__'

class NomencladorSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Nomenclador
		fields = '__all__'

class ModulosSerializer(serializers.ModelSerializer):
	class Meta:
		model = Modulos
		fields = '__all__'

class AlumModuloSerial(serializers.ModelSerializer):
	class Meta:
		model = AlumnosPorModulos
		fields = '__all__'