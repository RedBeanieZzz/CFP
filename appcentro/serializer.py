from dataclasses import field, fields
from rest_framework import serializers
from .models import Nacionalidad, Nomenclador, Alumnos, Cursos, Modulos, AlumnosPorModulos



class NacSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nacionalidad
		fields = '__all__'

class NomencSerializer(serializers.ModelSerializer):
	class Meta:
		model = Nomenclador
		fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumnos
		fields = '__all__'
		
class CursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cursos
		fields = '__all__'

class ModuloSerializer(serializers.ModelSerializer):
	class Meta:
		model = Modulos
		fields = '__all__'	

class AlumPorModSerializer(serializers.ModelSerializer):
	class Meta:
		model = AlumnosPorModulos
		fields = '__all__'
