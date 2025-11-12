from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bloco, Apartamento, Residente
from .serializers import BlocoSerializer, ApartamentoSerializer, ResidenteSerializer


class BlocosListCreate(generics.ListCreateAPIView):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


class BlocosRetrieverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


class ApartamentosListCreate(generics.ListAPIView):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class ApartamentosRetriverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class ResidenteListCreate(generics.ListCreateAPIView):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer


class ResidenteRetrieverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer
