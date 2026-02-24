from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from app.models import Bloco

class BlocosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username="admin", password="admin")
        self.url = reverse('listar_criar_blocos')
        self.client.force_authenticate(user=self.usuario)
        self.bloco_01 = Bloco.objects.create(
            numero = '1'
        )
        self.detail_url = reverse('bloco-detail', args=[self.bloco_01.id])

    def test_requisicao_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_requisicao_post(self):
        dados = {
            'numero': '2'
        }
        response = self.client.post(self.url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put(self):
        dados = {
            'numero': 45
        }
        response = self.client.put(self.detail_url, data=dados)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_delete(self):

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    

