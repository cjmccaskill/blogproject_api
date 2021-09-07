from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog # The model to be serialized
        fields = ['id', 'title', 'body'] #the fields that are included in output