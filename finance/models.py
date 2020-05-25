from django.db import models


class Company(models.Model):
	name = models.CharField(max_length=50)
	article = models.IntegerField()

	def __str__(self):
		return self.name

		