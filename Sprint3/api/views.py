from rest_framework.generics import ListAPIView
from coreapp.models import Contacto
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class ClienteListAPI(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClienteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Contacto.objects.all()  # Devuelve todos los clientes para usuarios 'staff'
        else:
            return Contacto.objects.none()  # No devuelve nada si no es 'staff'

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response(
                {"detail": "No tienes permiso para ver estos datos"},
                status=status.HTTP_403_FORBIDDEN
            )
            
        return super().get(request, *args, **kwargs)
