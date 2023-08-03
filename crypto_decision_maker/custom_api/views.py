from django.shortcuts import render
# custom_api/views.py
import requests
from django.http import JsonResponse

def fetch_cryptocurrency_data(request):
    api_url = "https://api.coingecko.com/api/v3/simple/price"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        return JsonResponse({"error": "Unable to fetch data from the external API"}, status=500)

# Create your views here.
