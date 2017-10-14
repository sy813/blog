from django.shortcuts import render, redirect, get_object_or_404, reverse

from myblog.models import Article
from .forms import CommentForm


# Create your views here.
def article_comment(request):
    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()

    form = CommentForm
    comment_list = article.comment_set.all()
    context = {'article': article,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'article.html', context=context)
