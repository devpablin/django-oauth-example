from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from .models import Todo, User
from .serializers import TodoSerializer, UserSerializer


class TodoListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['custom']

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        todos = Todo.objects.filter(user=request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetails(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['read_user']

    def get(self, request, *args, **kwargs):
        print(request.user.organization_id)
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetailsFree(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
