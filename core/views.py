from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Post
from core.forms import PostForm

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-id')
	return render(request, 'core/index.html', {'posts':posts})
	# return HttpResponse('Hello World')

def new(request):

	form = PostForm(request.POST or None)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('index')

	return render(request, 'core/new.html', {'form':form})	

def update(request, id):

	post = Post.objects.get(id=id)
	form = PostForm(request.POST or None, instance=post)

	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('index')

	return render(request, 'core/edit.html', {'form':form})	

	

def delete(request, id):
	
	post = Post.objects.get(id=id)

	if post:
		post.delete()
		return redirect('index')		