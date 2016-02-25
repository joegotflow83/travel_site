from django.db import models


class City(models.Model):


	name = models.CharField(max_length=32)
	population = models.IntegerField(default=0)
	fun_fact = models.TextField()

	def __str__(self):
		"""Prettify output"""
		return self.name
