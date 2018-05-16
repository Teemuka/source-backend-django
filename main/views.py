from django.shortcuts import render
from main.serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


# Create your views here.
class NewsTextViewSet(viewsets.ModelViewSet):
    queryset = NewsText.objects.all()
    serializer_class = NewsTextSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            #create must be overrided so we can get user of request
            instance = serializer.save(created_by=request.user)

            return Response(serializer.validated_data)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Error when serializing data'
            }, status=status.HTTP_400_BAD_REQUEST)


class HappeningViewSet(viewsets.ModelViewSet):
    queryset = Happening.objects.all()
    serializer_class = HappeningSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            instance = serializer.save(created_by=request.user)

            return Response(serializer.validated_data)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Error when serializing data'
            }, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return render(request, 'index.html')
