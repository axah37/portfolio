from django.db import models

# Create your models here.

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.TextField()
	title = models.CharField(max_length=140)
	date = models.DateTimeField()

	def __str__(self):
		return self.title