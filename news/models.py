from django.db import models
from django.conf import settings

class Headline(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="News/")
	url   = models.URLField()

	def __str__(self):
		return self.title

class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	last_seen = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return "{}-{}".format(self.user, self.last_seen)
