from .models import Bloco, Apartamento, Residente
from rest_framework import serializers


class BlocoSerializer(serializers.Serializer):

    class Meta:
        model = Bloco
        fields = "__all__"
        read_only_fields = ['id']


class ApartamentoSerializer(serializers.Serializer):

    class Meta:
        model = Apartamento
        fields = "__all__"
        read_only_fields = ['id']


class ResidenteSerializer(serializers.Serializer):

    class Meta:
        model = Residente
        fields = "__all__"
        read_only_fields = ['id']
