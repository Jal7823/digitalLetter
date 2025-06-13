from rest_framework import serializers
from ..models import Users


class SerializerClients(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'name', 'password']


class SerializerEmploye(serializers.ModelSerializer):

    def validate(self, data):
        data['role'] = 'employe'
        return data

    class Meta:
        model = Users
        fields = ['username', 'name', 'email', 'password']


#TODO FALTA CREAR SEREALIZADOR PARA LISTAR LOS USUARIOS SIEMPRE CON AUTORIZACION DE STAFF O DE EMPLEADO, TRATA DE GENERAR ALGUN TIPO DE FILTRO PARA QUE LOS EMPLEADOS TAMBIEN PUEDAR VER A LOS CLIENTES PERO CON CIERTAS RESTRICCIONES