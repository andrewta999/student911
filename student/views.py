from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post 

# Create your views here.

def learning(request):
	return render(request, 'detail.html', )

def share(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form = form.save()
			return redirect('/learning')
	else:
		form = PostForm()
	return render(request, 'post.html', {'form': form})

def subject(request, number):
	post = Post.objects.filter(topic=number).order_by("-date")
	# for p in post:
	# 	url_path = p.upload
	# 	url_path = url_path.split('/')
	# 	url_path = '/'.join(url_path)
	# 	p.upload = url_path
	return render(request, 'subject.html', {"post": post})

def home(request):
	return render(request, 'home.html')



