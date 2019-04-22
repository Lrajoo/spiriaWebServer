from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from .views import UserdataAPIView, UserdataDetailAPIView, UserdataUpdateAPIView, UserdataDeleteAPIView

urlpatterns = [
    url(r'^$', UserdataAPIView.as_view()),
    url(r'^(?P<userid>\d+)/$', UserdataDetailAPIView.as_view()),
    url(r'^(?P<userid>\d+)/update/$', UserdataUpdateAPIView.as_view()),
    url(r'^(?P<userid>\d+)/delete/$', UserdataDeleteAPIView.as_view()),
]
