# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, Wrlf!!")

# def test(request):
#     return HttpResponse("Fuck off")
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Article

def index(request):
    latest_articles_list = Article.objects.order_by('-published_date')[:5] # allows us to sort, last 5 articles
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена!")


    latest_comments_list = a.comment_set.order_by('-id')[:10]
    
    return render(request, 'articles/detail.html', {'article':a, 'latest_comments_list': latest_comments_list }) # a объекст запрошенный на трае и артикл в детайлсе есть


def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('articleblog:detail', args =(a.id,) ))