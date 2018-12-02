from django.db import models

# Create your models here.
class Subject(models.Model):
	title = models.CharField(max_length=500)
	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=500)
	name = models.CharField(max_length=500)
	url = models.CharField(max_length=500)
	description = models.CharField(max_length=5000)
	topic = models.ForeignKey(Subject, on_delete=models.CASCADE)
	upload = models.FileField(upload_to='student/static/imgs/')
	date = models.DateTimeField(auto_now_add=True)