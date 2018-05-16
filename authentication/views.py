import json
from rest_framework import views, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, User
from rest_framework import viewsets
from rest_framework import permissions

"""1 tästä kaikki alkaa"""
class UsersViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']


class LoginView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):

        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                serialized = UserSerializer(user)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):

        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)
