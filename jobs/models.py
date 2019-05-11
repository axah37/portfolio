from django.db import models

# Create your models here.

class Job(models.Model):
	image = models.ImageField(upload_to='images/')
	summary = models.TextField()
	title = models.CharField(max_length=140)
	date = models.DateTimeField()

	def __str__(self):
		return self.title

	def blurp(self):
		return self.summary[:200]
		

	def big_blurp(self):
		return self.summary[:400]

	
	def read_more_s(self):
		if len(self.summary) > 400:
			return True
		return False

	def read_more(self):
		if len(self.summary) > 200:
			return True
		return False