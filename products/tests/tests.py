import pytest
from django.urls import reverse
from rest_framework import status

from products.models import Product


@pytest.mark.django_db
class TestProduct:
    
    def test_list_products(self, api_client):
        url = reverse('products-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
    
    def test_create_agent(self, api_client):
        url = reverse('products-list')
        product_data = {
            "code": "Bread1",
            "name": "Baguette",
            "description": "Baguette",
            "category": "Bread",
            "price": 2,
            "quantity": 300,
            "inventoryStatus": "INSTOCK",
            }
        response = api_client.post(url, product_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Product.objects.filter(name='Baguette').exists()
    
    def test_retrieve_product(self, api_client, sample_product):
        url = reverse('products-detail', kwargs={'pk': sample_product.pk})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
    
    def test_update_product(self, api_client, sample_product):
        url = reverse('products-detail', kwargs={'pk': sample_product.pk})
        updated_data = {'name': 'Rice basmati super', 'quantity': 230}
        response = api_client.patch(url, updated_data)
        assert response.status_code == status.HTTP_200_OK
        sample_product.refresh_from_db()
        assert sample_product.name == 'Rice basmati super'
        assert sample_product.quantity == 230
    
    def test_delete_product(self, api_client, sample_product):
        url = reverse('products-detail', kwargs={'pk': sample_product.pk})
        response = api_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Product.objects.filter(pk=sample_product.pk).exists()