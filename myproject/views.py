from django.shortcuts import render

# Create your views here.

import oauth2 as oauth
#import httplib2
import time, os, simplejson
import urllib
#import urllib2
import urllib.request as urllib2
#import urllib.request as request
#import pycurl
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import resolve
#from django.core.shortcuts import render, redirect
from django import forms
from django.utils import timezone
#import urlparse
from urllib.parse import urlparse
import requests
import json
from collections import OrderedDict

#Linkedin
client_id = '77np7gttsxqikz'
client_key = 'o0KEyyMofH8rLr8X'
response_type = 'code'
redirect_uri = 'https://127.0.0.1:8000/auth/linkedin'
state='DCEeFWf45A53sdfKef424'

def login(request):
    redirect_uri = urllib2.quote('http://127.0.0.1:8000/auth/linkedin')
    codeURL = "https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=77np7gttsxqikz&state=DCEEFWF45453sdffef425&scope=r_fullprofile&redirect_uri=" + redirect_uri
    return HttpResponseRedirect(codeURL)

def loginsuccess(request):
    authcode = request.GET.get('code')
    redirect_uri = 'http://127.0.0.1:8000/auth/linkedin'

    postdata = {
        'grant_type': 'authorization_code',
        'code': authcode,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_key,
    }
    access_token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
    r = requests.post(access_token_url, data=postdata)
    print(r.text)
    j = json.loads(r.text)
    access_token = j['access_token']
    headers = {'Authorization' : 'Bearer'+access_token}
    access_data_url ='https://api.linkedin.com/v1/people/~?format=json'
    #access_data_url = 'https://api.linkedin.com/v1/people/~:(id,first-name,skills,educations,languages,twitter-accounts)?format=json'
    r = requests.get(access_data_url,headers=headers)
    print(r.text) 
    return HttpResponseRedirect('/')

def Manage(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponseRedirect('http://127.0.0.1:8000')

GLASSDOOR_API = 'http://www.glassdoor.com'
REVIEWS_URL = 'Reviews/company-reviews.htm'
pid =41227
key='ciEgRaHGnng'

'''
def get_glassdoor1(request):
    #userAgentString = request.headers.get('User-Agent')
    userAgentString = request.META.get('HTTP_USER_AGENT', '')
    print(userAgentString)
    hdr = {'User-Agent': userAgentString}
    url = "http://api.glassdoor.com/api/api.htm?t.p=pid&t.k=key&userip=128.237.202.227&useragent=Mozilla/%2F4.0&format=json&v=1&action=employers"
    r = requests.get(url)  
    #print(r.content)
    soup = BeautifulSoup(r.content)
    print(soup)
    #results = parse(soup)
    #req = urllib2.Request(url,headers=hdr)
    #response = urllib2.urlopen(req)
    #soup = BeautifulSoup(response)
    
'''    
def get_glassdoor(request):
    
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    params_gd = OrderedDict({
    "v": "1",
    "format": "json",
    "t.p": "41227",
    "t.k": key,
    "action": "employers",
    #"employerID": "11111",
    "q" : "Salesforce",
    # programmatically get the IP of the machine
    #"userip": json.loads(request.urlopen("http://ip.jsontest.com/").read().decode('utf-8'))['ip'],
    "userip" : ip,
    "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
    })

# construct the URL from parameters
    basepath_gd = 'http://api.glassdoor.com/api/api.htm'

# request the API
    response_gd = requests.get(basepath_gd,
                           params=params_gd,
                           headers={
                               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
                           })
# check the response code (should be 200)  & the content
    response_gd
    j = json.loads(response_gd.content.decode('utf-8'))
    response = j['response']
    employers =  response['employers']
    
    for i in employers :
        if i['exactMatch']:
            j = i['featuredReview']
            print(response)
    #print(j['jobTitle'])





def  home(request):
    return render(request,"home.html",{})

def  test(request):
    return render(request,"test1.html",{})

