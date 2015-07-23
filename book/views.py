from django.shortcuts import render, get_object_or_404

from .models import Article


def index(request):
    articles = Article.objects.order_by('title')
    context = {'articles': articles}
    return render(request, 'book/index.html', context)


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'book/article.html', {'article': article})
