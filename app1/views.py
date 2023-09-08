from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse

# Create your views here.
@api_view(['GET', 'POST'])
def Home(request):
    api_url = 'http://localhost:8001/api2/home/'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"error": "Failed to fetch data from Project A's API"}, status=status.HTTP_400_BAD_REQUEST)
