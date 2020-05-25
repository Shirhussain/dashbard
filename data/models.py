from django.db import models
from django.urls import reverse
from django.conf import settings

class Note(models.Model):
	user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="Note/",blank=True, null=True)
	url   = models.URLField(blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title

	def get_delete_url(self):
		return "{}/delete".format(self.pk)


	def get_update_url(self):
		return "{}/update/".format(self.pk)