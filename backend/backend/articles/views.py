from django.shortcuts import render
from django.http import JsonResponse

from .models import Article

def index(request):
    articles = []
    for article in Article.objects.all():
        articles.append({
            "name": article.name,
            "content": article.content
        })
    return JsonResponse(articles, safe=False)