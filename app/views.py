from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bloco, Apartamento, Residente
from .serializers import BlocoSerializer, ApartamentoSerializer, ResidenteSerializer


class BlocosListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


class BlocosRetrieverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


class ApartamentosListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class ApartamentosRetriverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class ResidenteListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer


class ResidenteRetrieverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer
