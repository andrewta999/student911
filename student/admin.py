from django.contrib import admin
from .models import Subject, Post
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
	list_display = ('title',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'name', 'url', 'description', 'topic', 'upload',)
