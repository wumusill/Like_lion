from django.shortcuts import render

# Create your views here.
def home(request):
    i = ['a', 'b']
    return render(request, 'home.html', {'i':i})

def home2(request):
    return render(request, 'home2.html')