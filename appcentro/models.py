from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime 

# Create your models here.

class Nacionalidad(models.Model):
	IDNacionalidad = models.IntegerField(validators = [MaxValueValidator(999)], primary_key = True)
	Nacionalidad = models.CharField(max_length = 15)

	class Meta:
		verbose_name_plural = 'Nacionalidades'

	def __str__(self):
		return str(self.IDNacionalidad) + "-- " + self.Nacionalidad

class Nomenclador(models.Model):
	CodigoDeArea = models.CharField(max_length = 7, primary_key = True)
	CodigoDePerfil = models.IntegerField(validators = [MaxValueValidator(99)])
	NombreDeArea = models.CharField(max_length = 30)
	NombreDePerfil = models.CharField( max_length = 80)    
	CargaHoraria = models.IntegerField(validators = [MaxValueValidator(9999)])
	Requisitos = models.CharField(max_length = 30)
	NivelDeCertificacion = models.IntegerField(validators = [MaxValueValidator(9)])
	Programacion = models.CharField(max_length = 25)
	TipoDeCapacitacion = models.CharField(max_length = 4)
	Anexo = models.IntegerField(validators = [MaxValueValidator(9999)])
	Observaciones = models.CharField(max_length = 50)

	class Meta:
			verbose_name_plural = 'Nomencladores'

	def __str__(self):
		retorno = ('Area : {0} - Perfil : {1}')
		return retorno.format(self.NombreDeArea, self.NombreDePerfil)

class Alumnos(models.Model):
	Documento = models.IntegerField(validators = [MaxValueValidator(999999999)], primary_key = True)
	ApellidoyNombre = models.CharField(max_length = 30)
	Direccion = models.CharField(max_length = 30)
	Localidad = models.CharField(max_length = 25)
	Telefono = models.BigIntegerField(validators = [MinValueValidator(0000000000), MaxValueValidator(9999999999)])
	Estudios = models.CharField(max_length = 15)
	Nacimiento = models.DateField()
	LugarDeNacimiento = models.CharField(max_length = 30)
	ProvinciaDeNacimiento = models.CharField(max_length = 20)
	IDNacionalidad = models.ForeignKey(Nacionalidad, on_delete = models.CASCADE)
	Sexo = models.CharField(max_length = 15)
		
	class Meta:
		verbose_name_plural = 'Alumnos'

	def __str__(self):
		salida = ('Alumno : {0} - DNI : {1}')
		return salida.format(self.ApellidoyNombre, self.Documento)
		
class Cursos (models.Model):
	IDCurso = models.IntegerField(validators = [MaxValueValidator(99999)], primary_key = True)
	CFP = models.IntegerField(validators = [MaxValueValidator(9999)])
	CicloLectivo = models.IntegerField(validators = [MaxValueValidator(99)])
	Nombre = models.CharField(max_length = 80)
	CodigoDeArea = models.ForeignKey(Nomenclador,related_name = 'appcentro.Nomenclador.CodigoDeArea+', on_delete = models.CASCADE)
	CodigoDePerfil = models.ForeignKey(Nomenclador, related_name = 'appcentro.Nomenclador.CodigoDePerfil+',on_delete = models.CASCADE)
	Resolucion = models.CharField(max_length = 20)
	Anexo = models.CharField(max_length = 5)
	CantidadDeClases = models.IntegerField(validators = [MaxValueValidator(999)])
	Inicio = models.DateField()
	Final = models.DateField()
	Horario = models.CharField(max_length = 15)

	class Meta:
		verbose_name_plural = 'Cursos'

	def __str__(self):
		output = ('Curso: {0}')
		return output.format(self.Nombre)

class Modulos(models.Model):
	IDModulo = models.IntegerField( primary_key = True)
	IDCurso = models.ForeignKey(Cursos, on_delete = models.CASCADE)
	Nombre = models.CharField(max_length = 50)
	
	class Meta:
		verbose_name_plural = 'Modulos'

	def __str__(self):
		if len(self.Nombre) > 30 :
			return self.Nombre + "..."
		else :
			return self.Nombre

class AlumnosPorModulos(models.Model):
	Documento = models.ForeignKey(Alumnos, on_delete = models.CASCADE)
	IDModulo = models.ForeignKey(Modulos, on_delete = models.CASCADE)
	IDCurso = models.ForeignKey(Cursos, related_name = 'appcentro.Cursos.IDCurso+', on_delete = models.CASCADE)
	CFP = models.ForeignKey(Cursos, related_name = 'appcentro.Cursos.CFP+', on_delete = models.CASCADE)
	Nota = models.IntegerField(validators = [MaxValueValidator(999)])
	Vencimiento = models.DateTimeField()

	class Meta:
			verbose_name_plural = 'Alumnos por Modulos'

	def __str__(self):
		alumni = ('{0} - Nota: {1}')
		return alumni.format(self.Documento, self.Nota)