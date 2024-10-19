import pytest
from rest_framework.test import APIClient

from products.models import Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def sample_product(db):
    product_data = {
        "code": "Rice12",
        "name": "Rice",
        "description": "Rice basmati",
        "category": "Rice",
        "price": 10,
        "quantity": 234,
        "inventoryStatus": "INSTOCK",
        }
    return Product.objects.create(**product_data)