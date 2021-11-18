from django.shortcuts import render
from .models import about
from .models import slider
from .models import client

def home(request):
    aboutdata=about.objects.all()[0]
    slidertdata=slider.objects.all()
    clientdata=client.objects.all()
    context={
        'about': aboutdata,
        'slider': slidertdata,
        'client':clientdata
    }
    return render(request,'index.html',context)
    
def aboutus(request):
    return render(request,'about.html')


