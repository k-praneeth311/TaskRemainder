from django.forms import ModelForm
from tasks.models import *

class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields='__all__'