from rest_framework import serializers

from cliente.api.serializers import ClienteSerializer
from compra import models
from produto.api.serializers import ProdutoSerializer


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compra
        fields = '__all__'

class CompraSerializerOut(serializers.ModelSerializer):
    cliente_cpf = ClienteSerializer()
    produto_id = ProdutoSerializer()

    class Meta:
        model = models.Compra
        fields = '__all__'