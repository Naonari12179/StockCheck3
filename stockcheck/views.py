from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import お菓子UZAWA, お菓子FUKUCHI, お菓子, 半生お菓子, チーズ, 洋日配, 飲料, お酒
import datetime
from datetime import  timedelta
from dateutil.relativedelta import relativedelta
from django.core.mail import send_mail

# Create your views here.
def index(request):
    today = str(datetime.datetime.now())
    almost_expired_list1 = お菓子UZAWA.objects.order_by('dis_date')[:10]
    almost_expired_list2 = お菓子FUKUCHI.objects.order_by('dis_date')[:10]
    almost_expired_list3 = お菓子.objects.order_by('dis_date')[:10]
    almost_expired_list4 = 半生お菓子.objects.order_by('dis_date')[:10]
    almost_expired_list5 = チーズ.objects.order_by('dis_date')[:10]
    almost_expired_list6 = 洋日配.objects.order_by('dis_date')[:10]
    almost_expired_list7 = 飲料.objects.order_by('dis_date')[:10]
    almost_expired_list8 = お酒.objects.order_by('dis_date')[:10]
    expiredlist1 = []
    expiredlist2 = []
    expiredlist3 = []
    expiredlist4 = []
    expiredlist5 = []
    expiredlist6 = []
    expiredlist7 = []
    expiredlist8 = []
    for s in almost_expired_list1:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=21):
            expiredlist1 = expiredlist1 + [name, str(date)]
        else:
            expiredlist1 = expiredlist1
    for s in almost_expired_list2:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=21):
            expiredlist2 = expiredlist2 + [name, str(date)]
        else:
            expiredlist2 = expiredlist2
    for s in almost_expired_list3:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=21):
            expiredlist3 = expiredlist3 + [name, str(date)]
        else:
            expiredlist3 = expiredlist3
    for s in almost_expired_list4:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=10):
            expiredlist4 = expiredlist4 + [name, str(date)]
        else:
            expiredlist4 = expiredlist4
    for s in almost_expired_list5:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=7):
            expiredlist5 = expiredlist5 + [name, str(date)]
        else:
            expiredlist5 = expiredlist5
    for s in almost_expired_list6:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=3):
            expiredlist6 = expiredlist6 + [name, str(date)]
        else:
            expiredlist6 = expiredlist6
    for s in almost_expired_list7:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+timedelta(days=14):
            expiredlist7 = expiredlist7 + [name, str(date)]
        else:
            expiredlist7 = expiredlist7
    for s in almost_expired_list8:
        name = s.商品名
        date = s.dis_date.date()
        if date <= datetime.datetime.now().date()+relativedelta(months = 1):
            expiredlist8 = expiredlist8 + [name, str(date)]
        else:
            expiredlist8 = expiredlist8
    if len(expiredlist1) > 0 or len(expiredlist2)>0 or len(expiredlist3)>0 or len(expiredlist4)>0 or len(expiredlist5)>0 or len(expiredlist6)>0 or len(expiredlist7)>0 or len(expiredlist8)>0:
        subject = 'StockCheckアプリから通知 %s'%today
        message = '賞味期限の近い商品があります。\n お菓子鵜沢さん(3週間以内):%s　\n お菓子福地さん(3週間以内):%s \n お菓子(3週間以内):%s \n 半生お菓子(10日以内):%s \n チーズ(1週間以内):%s \n 洋日配(3日以内):%s \n 飲料(2週間以内):%s \n お酒(1月以内):%s \n サイトhttp://naonaonao12179.pythonanywhere.com/admin/ \n 更新、チェックhttp://naonaonao12179.pythonanywhere.com/stockcheck/' % (expiredlist1,expiredlist2, expiredlist3, expiredlist4, expiredlist5, expiredlist6, expiredlist7, expiredlist8)
        frommail = []
        recipient = ['stockcheck223@gmail.com']
        send_mail(subject, message, frommail, recipient)
    else:
        subject = 'StockCheckアプリから通知%s'%today
        message = '賞味期限の近い商品はありません。\n サイトhttp://naonaonao12179.pythonanywhere.com/admin/ \n 更新、チェックhttp://naonaonao12179.pythonanywhere.com/stockcheck/'
        frommail = []
        recipient = ['stockcheck223@gmail.com']
        send_mail(subject, message, frommail, recipient)
    
    return HttpResponse(message)

def detail(request, stock_id):
    return HttpResponse("You're looking at stock %s." %stock_id)
