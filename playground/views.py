from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def playground_hello_view(request):
    return HttpResponse("Hello from the playground app!")