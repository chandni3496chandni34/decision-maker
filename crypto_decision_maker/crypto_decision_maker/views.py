# crypto/views.py
'''from django.shortcuts import render
import asyncio
import requests
import json

async def fetch_real_time_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }
    response = await requests.get(url, params=params)
    data = json.loads(response.text)
    return data[coin_id]["usd"]

def crypto_decision_maker(request):
    coin_id = "bitcoin"
    quantity = 2.5
    buy_price = 5000.0

    real_time_price = asyncio.run(fetch_real_time_price(coin_id))
    sell_price = float(real_time_price)

    profit_loss = sell_price - buy_price
    percent_profit_loss = (profit_loss / buy_price) * 100

    context = {
        "coin_id": coin_id.upper(),
        "real_time_price": real_time_price,
        "buy_price": buy_price,
        "profit_loss": profit_loss,
        "percent_profit_loss": percent_profit_loss,
    }

    return render(request, "crypto/crypto_decision_maker.html", context)

# Create your views here.'''
# crypto_decision_maker/views.py
import aiohttp
import json
from django.shortcuts import render

async def fetch_real_time_price(coin_id):
    url = f"https://binance-docs.github.io/apidocs/spot/en/"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data[coin_id]["usd"]
            else:
                return None  # Handle error case, e.g., return a default value or raise an exception

async def crypto_decision_maker(request):
    coin_id = "bitcoin"
    quantity = 2.5
    buy_price = 5000.0

    real_time_price = await fetch_real_time_price(coin_id)

    if real_time_price:
        real_time_price = float(real_time_price)
        sell_price = real_time_price
        profit_loss = sell_price - buy_price
        percent_profit_loss = (profit_loss / buy_price) * 100
    else:
        sell_price = None
        profit_loss = None
        percent_profit_loss = None

    context = {
        "coin_id": coin_id.upper(),
        "real_time_price": real_time_price,
        "buy_price": buy_price,
        "sell_price": sell_price,
        "profit_loss": profit_loss,
        "percent_profit_loss": percent_profit_loss,
    }

    return render(request, "crypto/crypto_decision_maker.html", context)

