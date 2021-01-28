# importing api
from django.shortcuts import render
# from newsapi import NewsApiClient
import requests


# Create your views here.
def index(request):

    url = ('http://newsapi.org/v2/top-headlines?country=in&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()


    l = listt['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'NewsApp/index.html', context={"mylist": mylist})

def entertainment(request):

    url = ('http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()


    l = listt['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'NewsApp/entertainment.html', context={"mylist": mylist})

def tech(request):
    url = ('http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()
    l = listt['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'NewsApp/technology.html', context={"mylist": mylist})



def business(request):

    url = ('http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()
    l = listt['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'NewsApp/business.html', context={"mylist": mylist})

def health(request):
    url= ('http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()
    l =listt['articles']
    desc =[]
    img = []
    news = []

    for i in  range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)
    return render(request, 'NewsApp/health.html',context={"mylist":mylist})

def science(request):
    url= ('http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()
    l =listt['articles']
    desc =[]
    img = []
    news = []

    for i in  range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)
    return render(request, 'NewsApp/science.html',context={"mylist":mylist})

def sports(request):
    url= ('http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=30f7d9c60d724b6eafd48dbfcbbec0a8')
    response = requests.get(url)
    listt = response.json()
    l =listt['articles']
    desc =[]
    img = []
    news = []

    for i in  range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)
    return render(request, 'NewsApp/sports.html',context={"mylist":mylist})




