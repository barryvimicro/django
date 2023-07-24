#from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    article=models.Article.objects.get(pk=1)
    title=article.title
    content=article.content
    return HttpResponse("<h3>文章标题：%s</h3><br> 文章内容：%s" % (title,content))

