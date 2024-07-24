from django.shortcuts import render, get_object_or_404
from .models import Article

def show_article(request, article_id):
    retrieved_article = get_object_or_404(Article, id=article_id)

    context = {
        "article": retrieved_article,
    }

    return render(request, 'articles/view_article.html', context)

def show_homepage(request):
    return render(request, 'articles/index.html')