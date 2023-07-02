from django.db import models

# Create your models here.
import requests
from django.conf import settings

def make_cellulant_api_request(url, data=None):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {settings.CELLULANT_API_KEY}:{settings.CELLULANT_API_SECRET}'
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle the API error
        raise Exception('API request failed')
