from django.shortcuts import render

# Create your views here.
def generic_static(request):
    return render(request,'generic_static.html')
