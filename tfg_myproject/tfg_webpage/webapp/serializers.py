from rest_framework import serializers

from .models import Storygraph_Book

class BookDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storygraph_Book
        fields = '__all__'