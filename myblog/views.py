from django.shortcuts import render, HttpResponse
from myblog.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


def global_data(request):
    category_list = Category.objects.all()
    archive_list = Article.objects.distinct_date()
    tag_list = Tag.objects.all()
    return locals()


# 主页
def index(request):
    article_list = Article.objects.all()
    article_list = get_page(request, article_list)
    return render(request, 'index.html', {'article_list': article_list})


# 归档
def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    article_lists = Article.objects.filter(date_publish__icontains=year+'-'+month)
    article_list = get_page(request, article_lists)
    return render(request, 'index.html', {'article_list': article_list})


# 标签
def tag(request):
    cid = request.GET.get('id', None)
    try:
        tag = Tag.objects.get(pk=cid)
    except Tag.DoesNotExist:
        return render(request, 'failure.html', {'reason': '标签不存在'})
    article_lists = Article.objects.filter(tag=tag)
    article_list = get_page(request, article_lists)
    return render(request, 'index.html', {'article_list': article_list})


# 分类
def category(request):
    id = request.GET.get('id', None)
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return render(request, 'failure.html', {'reason': '分类不存在'})
    article_list = Article.objects.filter(category=category)
    article_list = get_page(request, article_list)
    return render(request, 'index.html', locals())


#  分页
def get_page(request, article_list):
    paginator = Paginator(article_list, 4)
    try:
        page = request.GET.get('page', 1)
        article_list = paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list


# 文章详情
def article(request):
    id = request.GET.get('id', None)
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return render(request, 'failure.html', {'reason': '没有找到对应的文章'})
    return render(request, 'article.html', {'article': article})


def test(request):
    return render(request, 'test.html')
    # return HttpResponse('test page')
