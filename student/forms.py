
from django import forms
from . import models
class PostForm(forms.ModelForm):
	class Meta:
		model = models.Post 
		fields = ('title', 'name', 'url', 'description', 'topic', 'upload')
