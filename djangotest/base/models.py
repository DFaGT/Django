from django.db import models

# Create your models here.
class dbtest(models.Model):
	text = models.CharField(max_length=100)
	number = models.IntegerField()

	def __str__(self):
		return self.text
