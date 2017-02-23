from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
	return render(request, 'home.html', {})


def logout(request):
	if request.user.is_authenticated:
		logout(request)
		return HttpResponseRedirect('home')
