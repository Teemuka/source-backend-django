from rest_framework import serializers
from main.models import *


class NewsTextSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.username

    class Meta:
        model = NewsText
        fields = ('id', 'title', 'created_by', 'created_at', 'content')

        read_only_fields = ('created_at', 'updated_at', 'created_by')


class HappeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happening
        fields = ('id', 'title', 'date', 'created_at', 'content')

        read_only_fields = ('created_at', 'updated_at', 'created_by')
