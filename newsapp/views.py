from django.shortcuts import render
import datetime
# Create your views here.
def indexnews_info(request):
    return render(request,'newsapp/indexnews.html')


def movienews_info(request):
    head = 'This is movies news updates'
    m1 = 'Pathan breaks all records in of indian cinema'
    m2 = 'indian cinema geting popularity in worldwide'
    m3 = 'salman khan upcoming movie is bhaijhan'
    m4 = 'kiara married to sdidhart malhotra'
    my_dict = {'head':head,'m1':m1,'m2':m2,'m3':m3,'m4':m4}
    return render(request,'newsapp/news.html',my_dict)

def political_info(request):
    head = 'This is news political news portal'
    m1 = 'rahul ghandi completed successfully bharat jhodo yatra'
    m2 = 'next year lokshaba election is there'
    m3 = 'modi is going to win election'
    m4 = 'salman khan is give political tweet yesterday'
    my_dict = {'head':head,'m1':m1,'m2':m2,'m3':m3,'m4':m4}
    return render(request,'newsapp/news.html',my_dict)

def sports_info(request):
    head = 'This is sports news'
    m1 = 'ronaldo paying for sudhi riyadh'
    m2 = 'rishab panth is now curing slowly'
    m3 = 'kholi hit 100 again'
    m4 = 'sachin giving traing to has son rohan'
    my_dict = {'head':head,'m1':m1,'m2':m2,'m3':m3,'m4':m4}
    return render(request,'newsapp/news.html',my_dict)
