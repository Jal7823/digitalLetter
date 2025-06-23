from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.users.permisionsUsers import IsStaff, IsBoss
from apps.users.models import Users
from apps.users.api.serializers import SerializerClients, SerializerEmploye


@extend_schema_view(
    list=extend_schema(
        tags=['employee'],
        description='Should get all employee'
    ),
    create=extend_schema(
        tags=['employee'],
        description='Create a new instance of employee',
        request=SerializerEmploye,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    retrieve=extend_schema(
        tags=['employee'],
        description='Retrieve a specific instance of employee by ID',
        responses={
            200: SerializerEmploye,
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    update=extend_schema(
        tags=['employee'],
        description='Update a specific instance of employee by ID',
        request=SerializerEmploye,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    partial_update=extend_schema(
        tags=['employee'],
        description='Partial update a specific instance of employee by ID',
        request=SerializerEmploye,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    destroy=extend_schema(
        tags=['employee'],
        description='Delete a specific instance of employee by ID',
    ),
)
class RegisterEmploye(viewsets.ModelViewSet):
    queryset = Users.objects.filter(role='employe')
    serializer_class = SerializerEmploye
    # permission_classes = [IsStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get('password')
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@extend_schema_view(
    list=extend_schema(
        tags=['clients'],
        description='Should get all clients'
    ),
    create=extend_schema(
        tags=['clients'],
        description='Create a new instance of clients',
        request=SerializerClients,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    retrieve=extend_schema(
        tags=['clients'],
        description='Retrieve a specific instance of clients by ID',
        responses={
            200: SerializerClients,
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    update=extend_schema(
        tags=['clients'],
        description='Update a specific instance of clients by ID',
        request=SerializerClients,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    partial_update=extend_schema(
        tags=['clients'],
        description='Partial update a specific instance of clients by ID',
        request=SerializerClients,
        responses={
            400: Response({'description': 'The information is missed'}),
            404: Response({'description': 'Not found'}),
            500: Response({'description': 'Internal server error'}),
        },
    ),
    destroy=extend_schema(
        tags=['clients'],
        description='Delete a specific instance of clients by ID',
    ),
)
class RegisterClients(viewsets.ModelViewSet):
    queryset = Users.objects.filter(role='clients')
    serializer_class = SerializerClients
    # permission_classes = [IsStaff]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            password = request.data.get('password')
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)