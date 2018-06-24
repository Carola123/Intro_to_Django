from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse ("Hello, world. You are ate the polls index.")