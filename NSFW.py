# -*- coding:gbk -*-
# Copyright (c) 2021. Mars
import requests
from bs4 import BeautifulSoup
import time
import os

headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 '
        'Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400',
}
# urlAnimi = 'https://wallhaven.cc/search?categories=110&purity=010&topRange=1d&sorting=toplist&order=desc'
# urlPeople = 'https://wallhaven.cc/search?categories=001&purity=010&topRange=1d&sorting=toplist&order=desc&ai_art_filter=1'
urlAnimi = 'https://wallhaven.cc/user/FladedJade/uploads?purity=001'
urlPeople = 'https://wallhaven.cc/user/koko107/uploads?purity=001'
login_index_url = 'https://wallhaven.cc/login'
login_url = 'https://wallhaven.cc/auth/login'


def main():
    countA = 2
    countP = 2
    session = requests.Session()
    response = session.get(login_index_url, headers=headers)
    bf = BeautifulSoup(response.text, 'html.parser')
    hidden = bf.find_all('input', {'type': 'hidden'})
    for i in hidden:
        _token = i['value']
    data = {
        '_token': _token,
        'username': '111111',
        'password': '123456'
    }
    session.post(login_url, headers=headers, data=data)
    downloadPicA(urlAnimi, headers, session)
    while 1 == 1:
        target = downloadPicsA(headers, countA, urlAnimi, session)
        if target == 100:
            break
        else:
            print("----------------------page {0} Animi finish------------------------".format(countA))
            countA += 1
    downloadPicP(urlPeople, headers, session)
    while 1 == 1:
        target = downloadPicsP(headers, countP, urlPeople, session)
        if target == 100:
            break
        else:
            print("----------------------page {0} People finish------------------------".format(countP))
            countP += 1


def downloadPicP(urlPeople, headers, session):
    print("People开始")
    resp = session.get(urlPeople, headers=headers)
    resp.encoding = 'utf-8'
    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find_all("a", class_="preview")
    for a in alist:
        href = a.get('href')
        child_page_resp = session.get(href)
        child_page_resp.encoding = 'utf-8'
        child_page_text = child_page_resp.text
        child_page = BeautifulSoup(child_page_text, "html.parser")
        div = child_page.find("div", class_="scrollbox")
        img = div.find("img")
        src = img.get("src")
        img_resp = session.get(src)
        img_name = src.split("/")[-1]
        if not os.path.exists("img/NP/" + img_name):
            with open("img/NP/" + img_name, mode="wb") as f:
                f.write(img_resp.content)
                print("finish", img_name)
                time.sleep(1)
        else:
            print(img_name + " exists--------------------------")


def downloadPicsP(headers, countP, urlPeople, session):
    url = urlPeople + '&page={0}'.format(countP)
    print("第{0}页开始".format(countP))
    resp = session.get(url, headers=headers)
    resp.encoding = 'utf-8'
    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find_all("a", class_="preview")
    if not alist:
        return 100
    else:
        for a in alist:
            href = a.get('href')
            child_page_resp = session.get(href)
            child_page_resp.encoding = 'utf-8'
            child_page_text = child_page_resp.text
            child_page = BeautifulSoup(child_page_text, "html.parser")
            div = child_page.find("div", class_="scrollbox")
            img = div.find("img")
            src = img.get("src")
            img_resp = session.get(src)
            img_name = src.split("/")[-1]
            if not os.path.exists("img/NP/" + img_name):
                with open("img/NP/" + img_name, mode="wb") as f:
                    f.write(img_resp.content)
                    print("finish", img_name)
                    time.sleep(1)
            else:
                print(img_name + " exists--------------------------")


def downloadPicA(urlAnimi, headers, session):
    print("Animi开始")
    resp = session.get(urlAnimi, headers=headers)
    resp.encoding = 'utf-8'
    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find_all("a", class_="preview")
    for a in alist:
        href = a.get('href')
        child_page_resp = session.get(href)
        child_page_resp.encoding = 'utf-8'
        child_page_text = child_page_resp.text
        child_page = BeautifulSoup(child_page_text, "html.parser")
        div = child_page.find("div", class_="scrollbox")
        img = div.find("img")
        src = img.get("src")
        img_resp = session.get(src)
        img_name = src.split("/")[-1]
        if not os.path.exists("img/NA/" + img_name):
            with open("img/NA/" + img_name, mode="wb") as f:
                f.write(img_resp.content)
                print("finish", img_name)
                time.sleep(1)
        else:
            print(img_name + " exists--------------------------")


def downloadPicsA(headers, countA, urlAnimi, session):
    url = urlAnimi + '&page={0}'.format(countA)
    print("第{0}页开始".format(countA))
    resp = session.get(url, headers=headers)
    resp.encoding = 'utf-8'
    main_page = BeautifulSoup(resp.text, "html.parser")
    alist = main_page.find_all("a", class_="preview")
    if not alist:
        return 100
    else:
        for a in alist:
            href = a.get('href')
            child_page_resp = session.get(href)
            child_page_resp.encoding = 'utf-8'
            child_page_text = child_page_resp.text
            child_page = BeautifulSoup(child_page_text, "html.parser")
            div = child_page.find("div", class_="scrollbox")
            img = div.find("img")
            src = img.get("src")
            img_resp = session.get(src)
            img_name = src.split("/")[-1]
            if not os.path.exists("img/NA/" + img_name):
                with open("img/NA/" + img_name, mode="wb") as f:
                    f.write(img_resp.content)
                    print("finish", img_name)
                    time.sleep(1)
            else:
                print(img_name + " exists--------------------------")


if __name__ == '__main__':
    main()
