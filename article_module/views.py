from django.http import HttpRequest
from django.shortcuts import render
from .models import ArticleModel

# Create your views here.

def articles_view(request: HttpRequest):
    articles = list(ArticleModel.objects.filter(is_active=True))
    context = {'articles': articles, "name": "Pooya Danadeh"}
    return render(request=request, template_name="article_module/articles.html", context=context)