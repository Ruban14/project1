# views.py
import requests
from github import Github
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import YAMLForm

GITHUB_ACCESS_TOKEN = 'your_github_access_token'
GITHUB_REPO_OWNER = 'github_owner'
GITHUB_REPO_NAME = 'github_repo_name'

@api_view(['GET', 'POST'])
def Home(request):
    api_url = 'http://localhost:8001/api2/home/'

    if request.method == 'POST':
        form = YAMLForm(request.POST)
        if form.is_valid():
            yaml_data = form.cleaned_data['yaml_data']

            # Save the YAML data to the GitHub repository
            g = Github(GITHUB_ACCESS_TOKEN)
            repo = g.get_repo(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}")
            contents = repo.get_contents('path/to/file.yaml')
            repo.update_file(contents.path, "Update YAML data", yaml_data, contents.sha)

            return JsonResponse({"message": "YAML data saved to GitHub"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"error": "Invalid form data"}, status=status.HTTP_400_BAD_REQUEST)

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"error": "Failed to fetch data from Project A's API"}, status=status.HTTP_400_BAD_REQUEST)
