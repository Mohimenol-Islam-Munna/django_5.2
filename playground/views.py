from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def playground_hello_view(request):
    # return HttpResponse("Hello from the playground app!")
    a = 10
    b = 20
    return render(request, "playground/hello.html", {"name": "Full Stack Developer"})