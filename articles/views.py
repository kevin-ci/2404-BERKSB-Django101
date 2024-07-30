from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def show_article(request, article_id):
    retrieved_article = get_object_or_404(Article, id=article_id)

    context = {
        "article": retrieved_article,
    }

    return render(request, 'articles/view_article.html', context)

def show_homepage(request):
    all_articles = Article.objects.all()
    context = {
        "articles": all_articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your article was created!")
            return redirect("home")
    else:
        form = ArticleForm()
        context = { "form": form, }
        return render(request, 'articles/create_article.html', context)

@login_required
def edit_article(request, article_id):
    retrieved_article = get_object_or_404(Article, id=article_id)

    if not request.user == retrieved_article.author and not request.user.is_superuser:
        messages.error(request, "You cannot edit an article you did not create!")
        return redirect("home")

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=retrieved_article)
        if form.is_valid():
            form.save()
            messages.success(request, "Your article was updated!")
            return redirect("home")
    else:
        form = ArticleForm(instance=retrieved_article)
        context = { "form": form, }
        return render(request, 'articles/edit_article.html', context)

@login_required
def delete_article(request, article_id):
    retrieved_article = get_object_or_404(Article, id=article_id)

    if not request.user == retrieved_article.author and not request.user.is_superuser:
        messages.error(request, "You cannot delete an article you did not create!")
        return redirect("home")

    if request.method == "POST":
        retrieved_article.delete()
        messages.success(request, "Your article was deleted!")
        return redirect("home")

    else:
        context = { "article": retrieved_article, }
        return render(request, 'articles/delete_article.html', context)