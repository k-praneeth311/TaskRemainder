from django.db import models
from django.contrib.auth.models import User,auth
# Create your models here.
class Task(models.Model):
	title=models.CharField(max_length=500)
	complete=models.BooleanField(default=False)
	created=models.DateTimeField(auto_now_add=True)
	uid = models.ForeignKey(User, on_delete=models.CASCADE)
	#userid=models.CharField(max_length=100,default=u)
	def __str__(self):
		return self.title[:50]