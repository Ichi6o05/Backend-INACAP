from rest_framework import serializers
from coreapp.models import Contacto

class ClienteSerializer(serializers.ModelSerializer):
    curso = serializers.StringRelatedField()
    
    class Meta:
        model = Contacto
        fields = '__all__'
        read_only_fields = ["fecha_envio"]