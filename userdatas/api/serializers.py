from rest_framework import serializers
from userdatas.models import Userdata


class UserdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = [
            'userid',
            'age',
            'spiral',
            'tremor',
            'questionnaire',
            'prediction',
            'date',
            'response1',
            'response2',
            'response3',
            'response4',
            'response5',
            'response6',
        ]