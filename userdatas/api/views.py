from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserdataSerializer
from userdatas.models import Userdata
from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from django.shortcuts import get_object_or_404
import json

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class UserdataAPIView(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, generics.ListAPIView):
    permission_classes = []
    serializer_class = UserdataSerializer
    lookup_field = 'userid'

    def get_queryset(self):
        request = self.request
        qs = Userdata.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    # def get_object(self):
    #     request = self.request
    #     passed_id = request.GET.get('userid')
    #     queryset = self.get_queryset()
    #     if passed_id is not None:
    #         obj = get_object_or_404(queryset, id=passed_id)
    #         self.check_object_permissions(request, obj)
    #     return obj 

    # def get(self, request, *args, **kwargs):
    #     passed_id = request.GET.get('userid', None)
    #     if passed_id is not None:
    #         return self.retrieve(request, *args, **kwargs)
    #     return super().get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UserdataDetailAPIView(RetrieveAPIView):
     permission_classes = []
     serializer_class = UserdataSerializer
     queryset = Userdata.objects.all()
     lookup_field = 'userid'

class UserdataUpdateAPIView(UpdateAPIView):
     permission_classes = []
     serializer_class = UserdataSerializer
     queryset = Userdata.objects.all()
     lookup_field = 'userid'

class UserdataDeleteAPIView(DestroyAPIView):
     permission_classes = []
     serializer_class = UserdataSerializer
     queryset = Userdata.objects.all()
     lookup_field = 'userid'


