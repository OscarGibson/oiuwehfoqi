from django.db import models

class Page(models.Model):
	name = models.CharField(max_length= 2048, unique= True)
	path = models.CharField(max_length= 2048)

	def __str__(self):
		return self.name