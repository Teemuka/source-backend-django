from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    user_picture = serializers.StringRelatedField(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_picture')

    """2 tämä hoitaa JSON -> Python ja vice versa"""
    """TODO testaa yksinkertaistaako SAVE vai CREATE datan"""
    """def create(self, validated_data):

        print("VALIDATED DATA:")
        print(validated_data)

        return User.objects.create(**validated_data)"""
