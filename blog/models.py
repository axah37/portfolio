from django.db import models

# Create your models here.

class Blog(models.Model):
	image = models.ImageField(upload_to='images/')
	title = models.CharField(max_length = 140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:400]

	def read_more(self):
		if len(self.body) > 400:
			return True
		return False