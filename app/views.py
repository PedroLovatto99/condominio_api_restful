from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Bloco, Apartamento, Residente
from .serializers import BlocoSerializer, ApartamentoSerializer, ResidenteSerializer
from rest_framework.response import Response
from rest_framework import status

class BlocosListCreate(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer

    def get(self, request, *args, **kwargs):

        blocos = self.queryset.all()
        serializer = self.serializer_class(blocos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlocosRetrieverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer


class ApartamentosListCreate(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer

    def get(self, request, *args, **kwargs):

        apartamentos = self.queryset.all()
        serializer = self.serializer_class(apartamentos, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApartamentosRetriverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer


class ResidenteListCreate(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer

    def get(self, request, *args, **kwargs):

        residentes = self.queryset.all()
        serializer = self.serializer_class(residentes, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResidenteRetrieverUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer
