from django.shortcuts import render
from django.http import HttpResponse,request
import requests
from bs4 import BeautifulSoup

def index(request):

    # source Code
    page = requests.get('https://corona.gov.bd/lang/en')
    main = BeautifulSoup(page.content, 'html.parser')
    # container
    container = main.find_all(class_='container')
    # print(container[2])

    # row
    row = container[2].find_all(class_='row')
    # print(row[0])

    # section
    section = row[0].find_all(class_='col-lg-3 col-xs-6 live-update-box')
    # print(section[0])

    ''' 
        section[0] -> New Infected
        section[1] -> Death
        section[2] -> Cure
        section[3] -> Test
    '''
    '''
        section[]:
            -> col-lg-6 -> live-update-box-wrap-h1
            -> col-lg-6 text-right -> live-update-box-wrap-h1
    '''

    # newinfected
    info_1 = section[0].find_all(class_='live-update-box-wrap-h1')
    # print(info_1[0])
    N = info_1[0].find('b').get_text()
    Nt = info_1[1].find('b').get_text()

    # Death
    info_2 = section[1].find_all(class_='live-update-box-wrap-h1')
    # print(info_1[0])
    D = info_2[0].find('b').get_text()
    Dt = info_2[1].find('b').get_text()

    # Cure
    info_3 = section[2].find_all(class_='live-update-box-wrap-h1')
    # print(info_1[0])
    C = info_3[0].find('b').get_text()
    Ct = info_3[1].find('b').get_text()

    # Test
    info_4 = section[3].find_all(class_='live-update-box-wrap-h1')
    # print(info_1[0])
    T = info_4[0].find('b').get_text()
    Tt = info_4[1].find('b').get_text()

    # Last Update

    update = row[5].find(class_='last-update').get_text()
    s = str(update)
    latest = s.replace("\n", " ")
    percentage = (int(N)/int(T))*100
    P = "{:.2f}".format(percentage)
    return render(request,'index.html',{'N' : N , 'Nt' : Nt , 'D' : D , 'Dt':Dt,'C':C,'Ct' : Ct , 'T' : T ,'Tt':Tt,'latest' : latest,'P' : P})
