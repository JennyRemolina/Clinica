from django.db import models

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=70)
	ci = models.CharField(max_length=10, primary_key=True)
	telf = models.CharField(max_length=12)
	direccion = models.CharField(max_length=70)

	def __str__ ( self ):
		return self.nombre

	def get_absolute_url ( self ):
		return reverse ( 'Persona-detail',
			args =[ str ( self.id )])