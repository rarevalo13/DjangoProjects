from django.http import HttpResponse

def index(Response):
	return HttpResponse("Hello, world. You're at the polls index.")

