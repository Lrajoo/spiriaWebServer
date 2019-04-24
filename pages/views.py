from django.shortcuts import render
from django.http import HttpResponse
from userdatas.models import Userdata

# Create your views here.
def index(request):
    userdatas = Userdata.objects.order_by('-date')[:3]
    context = {
        'userdatas': userdatas
    }
    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')