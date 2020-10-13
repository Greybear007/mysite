from django.shortcuts import render

# Create your views here.
from datetime import datetime
from trips.models import Post


def hello_world(request):
	context = {'current_time': datetime.now()}
	return render(request, 'hello_world.html', context=context)

def home(request):
	post_list = Post.objects.filter(id__lte=10)
	context = {'post_list': post_list}
	return render(request, 'home.html', context=context)

