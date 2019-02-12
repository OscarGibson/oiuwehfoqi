import os
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Page(models.Model):
    name = models.CharField(max_length= 2048, unique= True)
    path = models.CharField(max_length= 2048)
    html = models.TextField()

    def __str__(self):
        return self.name


#	@property
#	def html(self):
#		return open(self.path, 'r').read()


@receiver(post_save, sender= Page)
def post_save(sender, instance, created, **kwargs):
    f = open(instance.path, 'w')
    f.write(instance.html)
    f.close()
