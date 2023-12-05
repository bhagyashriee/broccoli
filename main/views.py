# main/views.py
from django.shortcuts import render
from .models import Crypto
import requests

def crypto_list(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd'
    response = requests.get(url)
    cryptos_data = response.json()

    # Save data to the Crypto model
    for crypto_data in cryptos_data:
        Crypto.objects.create(name=crypto_data['name'], current_price=crypto_data['current_price'])

    # Fetch data from the Crypto model
    cryptos = Crypto.objects.all()

    return render(request, 'crypto/crypto_list.html', {'cryptos': cryptos})


