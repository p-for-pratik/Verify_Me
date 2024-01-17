from rest_framework import serializers

from .models import apiModel

# create a model from serializer
class apiserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = apiModel
        exclude = ('title', 'description')