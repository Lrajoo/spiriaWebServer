from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Userdata

# Create your views here.
def index(request):
    userdatas = Userdata.objects.order_by('-date')

    paginator = Paginator(userdatas, 6)
    page = request.GET.get('page')
    paged_userdatas = paginator.get_page(page)

    context = {
        'userdatas': paged_userdatas
    }
    return render(request, 'userdatas/userdatas.html', context)

def user(request, userdata_id):
    userdata = get_object_or_404(Userdata, pk=userdata_id)

    context = {
        'userdata': userdata
    }
    return render(request, 'userdatas/userdata.html')

def search(request):
    return render(request, 'userdatas/search.html')
    