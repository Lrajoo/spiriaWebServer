from django.urls import path

from . import views


urlpatterns = [ 
    path('', views.index, name='userdatas'),
    path('<int:userdata_id>', views.user, name='userdata'),
    path('search', views.search, name='search')

]