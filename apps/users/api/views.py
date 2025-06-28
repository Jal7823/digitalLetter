from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.users.permisionsUsers import IsStaff, IsBoss,IsStaffOrEmploye
from apps.users.models import Users
from apps.users.api.serializers import (
    SerializerClients,
    SerializerEmploye,
    UserListSerializer,
    ChangePasswordSerializer
)


@extend_schema_view(
    list=extend_schema(tags=["employee"], description="Should get all employee"),
    create=extend_schema(
        tags=["employee"],
        description="Create a new instance of employee",
        request=SerializerEmploye,
        responses={
            400: Response({"description": "The information is missed"}),
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    retrieve=extend_schema(
        tags=["employee"],
        description="Retrieve a specific instance of employee by ID",
        responses={
            200: SerializerEmploye,
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    update=extend_schema(
        tags=["employee"],
        description="Update a specific instance of employee by ID",
        request=SerializerEmploye,
        responses={
            400: Response({"description": "The information is missed"}),
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    partial_update=extend_schema(
        tags=["employee"],
        description="Partial update a specific instance of employee by ID",
        request=SerializerEmploye,
        responses={
            400: Response({"description": "The information is missed"}),
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    destroy=extend_schema(
        tags=["employee"],
        description="Delete a specific instance of employee by ID",
    ),
)
class RegisterEmploye(viewsets.ModelViewSet):
    queryset = Users.objects.filter(role="employe")
    serializer_class = SerializerEmploye
    permission_classes = [IsStaff]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsStaff()]
        elif self.action == 'list':
            return [IsStaffOrEmploye()]
        return super().get_permissions()


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            password = request.data.get("password")
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=["clients"], description="Should get all clients"),
    create=extend_schema(
        tags=["clients"],
        description="Create a new instance of clients",
        request=SerializerClients,
        responses={
            400: Response({"description": "The information is missed"}),
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    retrieve=extend_schema(
        tags=["clients"],
        description="Retrieve a specific instance of clients by ID",
        responses={
            200: SerializerClients,
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    update=extend_schema(
        tags=["clients"],
        description="Update a specific instance of clients by ID",
        request=SerializerClients,
        responses={
            400: Response({"description": "The information is missed"}),
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    partial_update=extend_schema(
        tags=["clients"],
        description="Partial update a specific instance of clients by ID",
        request=SerializerClients,
        responses={
            400: Response({"description": "The information is missed"}),
            404: Response({"description": "Not found"}),
            500: Response({"description": "Internal server error"}),
        },
    ),
    destroy=extend_schema(
        tags=["clients"],
        description="Delete a specific instance of clients by ID",
    ),
)
class RegisterClients(viewsets.ModelViewSet):
    queryset = Users.objects.filter(role="client")
    serializer_class = SerializerClients

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            password = request.data.get("password")
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(
        tags=["users"],
        description="List users, accessible by staff and employees",
        responses={200: UserListSerializer(many=True)},
    )
)
class UsersListViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsStaffOrEmploye,]
    serializer_class = UserListSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Users.objects.all()
        elif user.role == "employe":
            return Users.objects.filter(Q(role="client") | Q(id=user.id))
        return Users.objects.none()

    def list(self, request, *args, **kwargs):
        if not (request.user.is_staff or request.user.role == "employe"):
            return Response({"detail": "Not authorized."}, status=403)
        return super().list(request, *args, **kwargs)


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserListSerializer(user)
        return Response(serializer.data)
    def patch(self, request):
        user = request.user
        serializer = UserListSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({"old_password": "Contraseña actual incorrecta."},
                                status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"detail": "Contraseña actualizada correctamente."},
                            status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)