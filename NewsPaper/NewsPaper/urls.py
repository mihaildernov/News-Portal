"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news.views import SubscriberView, PostsList, PostDetail, NewsCreate, NewsUpdate, NewsDelete, SearchList, ArticleCreate, ArticleUpdate, ArticleDelete


urlpatterns = [
   path('i18n/', include('django.conf.urls.i18n')),
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),
   path('newss/', PostsList.as_view()),
   path('newss/search', SearchList.as_view()),
   path('newss/<int:pk>', PostDetail.as_view()),
   path('newss/news/create/', NewsCreate.as_view(), name='news_create'),
   path('newss/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('newss/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('newss/article/create/', ArticleCreate.as_view(), name='article_create'),
   path('newss/<int:pk>/update/', ArticleUpdate.as_view(), name='article_update'),
   path('newss/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
   path('', include('protect.urls')),
   path('sign/', include('sign.urls')),
   path('accounts/', include('allauth.urls')),
   path('subscribe/', SubscriberView.as_view(), name='subscribe'),
]
