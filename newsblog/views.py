from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
from newspaper import fulltext, Article
from django.conf import settings
from decouple import config
# Create your views here.

# NEWS_API = '3c918234eb854993a5694d9760d9158a'
# NEWS_API = settings.NEWS_API_KEY
NEWS_API = config('NEWS_API_KEY')
date30daysago = datetime.datetime.now() - datetime.timedelta(30)
start_date = f"{date30daysago:%Y-%m-%d}"

def index(request):
    
    url_world_topheadlines = 'https://newsapi.org/v2/top-headlines/sources?apiKey='
    url_world_topheadlines += NEWS_API

    world_topheadlines = requests.get(url_world_topheadlines).json()
    
#     {'category': 'general',
#   'country': 'au',
#   'description': "Australia's most trusted source of local, national and world "
#                  'news. Comprehensive, independent, in-depth analysis, the '
#                  'latest business, sport, weather and more.',
#   'id': 'abc-news-au',
#   'language': 'en',
#   'name': 'ABC News (AU)',
#   'url': 'http://www.abc.net.au/news'}

    a = world_topheadlines['sources']
    country=[]
    desc =[]
    source =[]
    cat =[]
    url=[]

    for i in range(len(a)):
        f = a[i]
        country.append(f['country'])
        desc.append(f['description'])
        source.append(f['name'])
        cat.append(f['category'])
        url.append(f['url'])
    world_topheadlines_list = zip(country, desc, source, cat, url)
    
    context = {'world_topheadlines_list': world_topheadlines_list}
    
    return render(request, 'newsblog/index.html', context)

def crypto_news(request):
    url_crypto = 'https://newsapi.org/v2/everything?q=Cryptocurrency&from=' + start_date + '&sortBy=popularity&apiKey='

    url_crypto += NEWS_API
    print(url_crypto)
    crypto_news = requests.get(url_crypto).json()

    b = crypto_news['articles']
    desc =[]
    title =[]
    img =[]
    url=[]

    for i in range(len(b)):
        f = b[i]
        desc.append(f['description'])
        title.append(f['title'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    myCryptolist = zip( desc, title, url, img)

    context = {'myCryptolist': myCryptolist}
    
    return render(request, 'crypto-news.html', context)
    
def us_news(request):
    url_usa = 'https://newsapi.org/v2/top-headlines?country=us&apiKey='
    url_usa += NEWS_API
    
    usa_news = requests.get(url_usa).json()

    b = usa_news['articles']
    desc_i =[]
    title_i =[]
    img_i =[]
    url_i=[]

    for i in range(len(b)):
        f = b[i]
        title_i.append(f['title'])
        desc_i.append(f['description'])
        img_i.append(f['urlToImage'])
        url_i.append(f['url'])
    myUSAlist = zip(title_i, desc_i, url_i, img_i)
    
    context = {'myUSAlist': myUSAlist}
    
    return render(request, 'newsblog/us-news.html', context)
    
def israel_news(request):
    url_israel = 'https://newsapi.org/v2/top-headlines?country=il&apiKey='
    url_israel += NEWS_API
    
    israel_news = requests.get(url_israel).json()

    b = israel_news['articles']
    desc_i =[]
    title_i =[]
    img_i =[]
    url_i=[]

    for i in range(len(b)):
        f = b[i]
        title_i.append(f['title'])
        desc_i.append(f['description'])
        img_i.append(f['urlToImage'])
        url_i.append(f['url'])
    myIsraellist = zip(title_i, desc_i, url_i, img_i)
    
    context = {'myIsraellist': myIsraellist}
    
    return render(request, 'newsblog/israel-news.html', context)

def single(request):
    url = request.GET.get('url')
    img = request.GET.get('img')
    title = request.GET.get('title')
    # type = request.GET.get('type', 'default')
    html = requests.get(url).text # gets full page
    text = fulltext(html) # gets text only

    # a = Article(url)
    # a.download()

    # return HttpResponse(text)
    
    context = { 'content': text, 'image': img, 'title': title }
    return render(request, 'newsblog/single.html', context)
    
"""     
    article = newspaper.Article(url) # STRING REQUIRED AS `url` ARGUMENT BUT NOT USED
    article.set_html(html)
     """
     


def article(request, article_id):
    return render(request, 'newsblog/index.html', {'articel_id': article_id})
"""   
def single(request):
    url = request.GET.get('url')
    return HttpResponse(url)
    
         
def single(request, url):
    
    article = newspaper.Article(url) # STRING REQUIRED AS `url` ARGUMENT BUT NOT USED
    context = article.set_html(article)
    # return render(request, 'newsblog/singel.html', context)
    # return HttpResponse(context)
    return HttpResponse(url) """