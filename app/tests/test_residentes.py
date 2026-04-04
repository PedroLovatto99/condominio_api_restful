from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from app.models import Bloco, Apartamento, Residente

class ResidentesTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username="admin", password="admin")
        self.url = reverse('listar_criar_residentes')
        self.client.force_authenticate(user=self.usuario)

        self.bloco = Bloco.objects.create(numero=1)
        self.apartamento = Apartamento.objects.create(numero=101, bloco=self.bloco)
        
        self.residente_01 = Residente.objects.create(
            nome="Residente Teste",
            apartamento=self.apartamento,
            cpf_cnpj="111.111.111-11",
            telefone="55999999999",
            email="teste@teste.com",
            data_inicio="2025-01-01",
            data_fim="2026-01-01",
            numero_cadastro=1,
            valor_aluguel=1500.00,
            valor_condominio=350.00
        )
        self.detail_url = reverse('residente-detail', args=[self.residente_01.id])

    def test_requisicao_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post(self):
        dados = {
            "nome": "Novo Residente",
            "apartamento": self.apartamento.id,
            "cpf_cnpj": "222.222.222-22",
            "telefone": "55888888888",
            "email": "novo@teste.com",
            "data_inicio": "2025-05-01",
            "data_fim": "2026-05-01",
            "numero_cadastro": 2,
            "valor_aluguel": 1600.00,
            "valor_condominio": 350.00
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put(self):

        dados = {
            "nome": "Residente Teste Alterado",
            "apartamento": self.apartamento.id,
            "cpf_cnpj": "111.111.111-11",
            "telefone": "55999999999",
            "email": "teste_alterado@teste.com", 
            "data_inicio": "2025-01-01",
            "data_fim": "2026-01-01",
            "numero_cadastro": 1,
            "valor_aluguel": 1550.00,
            "valor_condominio": 350.00
        }
        response = self.client.put(self.detail_url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)