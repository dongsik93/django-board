from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
    
def greeting(request, name):
    return render(request, "greeting.html", {"name":name})    
    
def cube(request, num):
    result = num**3
    return render(request, "cube.html", {"num":num, "result":result})