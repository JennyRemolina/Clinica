from django.db import models

from paciente.models import Persona

class Cardiotocografo(models.Model):
	serial = models.CharField(max_length=10, primary_key=True)
	paciente = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=70)
	cargo = models.CharField(max_length=12)

	def __str__ ( self ):
		return self.tipo

	def get_absolute_url ( self ):
		return reverse ( 'Cardiotocografo-detail',
			args =[ str ( self.id )])