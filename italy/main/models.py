from django.db import models


class Contact(models.Model):


	first_name = models.CharField(max_length=32)
	last_name = models.CharField(max_length=32)
	email = models.EmailField(unique=True)
