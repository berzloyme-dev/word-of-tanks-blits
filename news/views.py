from django.shortcuts import render, get_object_or_404
from .models import *


def news_list(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'news/news_list.html', {
        'articles': articles
    })


def news_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/news_detail.html', {
        'article': article
    })

def news_list(request):
    articles = Article.objects.all()
    return render(request, 'news/news_list.html', {
        'articles': articles
    })