"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from myblog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/$', views.category, name='category'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^tag/$', views.tag, name='tag'),
    url(r'^article/$', views.article, name='article'),
    # url(r'^search/$', views.search, name='search'),
    url(r'^search/', include('haystack.urls')),
    url(r'^test/', views.test, name='test'),
]
