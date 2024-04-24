import requests
from bs4 import BeautifulSoup
import time
import os

# 模拟浏览器请求，最基础的防被封机制
headers = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400',
}
# # 想要爬取的网页
urlAnimi = 'https://wallhaven.cc/search?categories=110&purity=010&topRange=1d&sorting=toplist&order=desc'
urlPeople = 'https://wallhaven.cc/search?categories=001&purity=010&topRange=1d&sorting=toplist&order=desc&ai_art_filter=1'
# https://wallhaven.cc/search?categories=001&purity=010&topRange=1w&sorting=toplist&order=desc
# https://wallhaven.cc/search?categories=111&purity=010&topRange=1d&sorting=toplist&order=desc
count = 2
countP = 2

def downloadPicP(urlPeople, headers):
    try:
        print("People开始")
        resp = requests.get(urlPeople, headers=headers)
        resp.encoding = 'utf-8'
        # 把源码交给BeautifulSoup
        main_page = BeautifulSoup(resp.text, "html.parser")
        # 这里需要自己从网页源码中找需要爬取内容的标签以及class等标识
        alist = main_page.find_all("a", class_="preview")
        for a in alist:
            # print(a.get('href'))
            # time.sleep(1)
            href = a.get('href')
            # 拿到子页面源码
            child_page_resp = requests.get(href)
            child_page_resp.encoding = 'utf-8'
            child_page_text = child_page_resp.text
            # 从子页面拿到图片下载路径
            child_page = BeautifulSoup(child_page_text, "html.parser")
            # 这里也需要自己从网页源码中找特殊的那个标签或者class等唯一标识
            div = child_page.find("div", class_="scrollbox")
            # print(div)
            # time.sleep(1)
            img = div.find("img")
            # print(img.get("src"))
            # time.sleep(1)
            src = img.get("src")
            # 下载图片
            img_resp = requests.get(src)
            # 拿到url中最后一个/后面的内容
            img_name = src.split("/")[-1]
            # 如果图片名不存在
            if not os.path.exists("img/People/" + img_name):
                with open("img/People/" + img_name, mode="wb")as f:
                    # 图片内容写入文件
                    f.write(img_resp.content)
                    print("finish", img_name)
                    time.sleep(1)
            else:
                print(img_name + " exists--------------------------")
    except Exception as exc:
        print(exc)


def downloadPicsP(headers, countP, urlPeople):
    try:
        url = urlPeople + '&page={0}'.format(countP)
        print("第{0}页开始".format(countP))
        resp = requests.get(url, headers=headers)
        resp.encoding = 'utf-8'
        # 把源码交给BeautifulSoup
        main_page = BeautifulSoup(resp.text, "html.parser")
        # 这里需要自己从网页源码中找需要爬取内容的标签以及class等标识
        alist = main_page.find_all("a", class_="preview")
        if alist == []:
            return 100
        else:
            for a in alist:
                # print(a.get('href'))
                # time.sleep(1)
                href = a.get('href')
                # 拿到子页面源码
                child_page_resp = requests.get(href)
                child_page_resp.encoding = 'utf-8'
                child_page_text = child_page_resp.text
                # 从子页面拿到图片下载路径
                child_page = BeautifulSoup(child_page_text, "html.parser")
                # 这里也需要自己从网页源码中找特殊的那个标签或者class等唯一标识
                div = child_page.find("div", class_="scrollbox")
                # print(div)
                # time.sleep(1)
                img = div.find("img")
                # print(img.get("src"))
                # time.sleep(1)
                src = img.get("src")
                # 下载图片
                img_resp = requests.get(src)
                # 拿到url中最后一个/后面的内容
                img_name = src.split("/")[-1]
                # 如果图片名不存在
                if not os.path.exists("img/People/" + img_name):
                    with open("img/People/" + img_name, mode="wb")as f:
                        # 图片内容写入文件
                        f.write(img_resp.content)
                        print("finish", img_name)
                        time.sleep(1)
                else:
                    print(img_name + " exists--------------------------")

    except Exception as exc:
        print(str(exc) + ' 2')


def downloadPicA(urlAnimi, headers):
    try:
        print("Animi开始")
        resp = requests.get(urlAnimi, headers=headers)
        resp.encoding = 'utf-8'
        # 把源码交给BeautifulSoup
        main_page = BeautifulSoup(resp.text, "html.parser")
        # 这里需要自己从网页源码中找需要爬取内容的标签以及class等标识
        alist = main_page.find_all("a", class_="preview")
        for a in alist:
            # print(a.get('href'))
            # time.sleep(1)
            href = a.get('href')
            # 拿到子页面源码
            child_page_resp = requests.get(href)
            child_page_resp.encoding = 'utf-8'
            child_page_text = child_page_resp.text
            # 从子页面拿到图片下载路径
            child_page = BeautifulSoup(child_page_text, "html.parser")
            # 这里也需要自己从网页源码中找特殊的那个标签或者class等唯一标识
            div = child_page.find("div", class_="scrollbox")
            # print(div)
            # time.sleep(1)
            img = div.find("img")
            # print(img.get("src"))
            # time.sleep(1)
            src = img.get("src")
            # 下载图片
            img_resp = requests.get(src)
            # 拿到url中最后一个/后面的内容
            img_name = src.split("/")[-1]
            # 如果图片名不存在
            if not os.path.exists("img/Animi/" + img_name):
                with open("img/Animi/" + img_name, mode="wb")as f:
                    # 图片内容写入文件
                    f.write(img_resp.content)
                    print("finish", img_name)
                    time.sleep(1)
            else:
                print(img_name + " exists--------------------------")
    except Exception as exc:
        print(exc)


def downloadPicsA(headers, count, urlAnimi):
    try:
        url = urlAnimi + '&page={0}'.format(count)
        print("第{0}页开始".format(count))
        resp = requests.get(url, headers=headers)
        resp.encoding = 'utf-8'
        # 把源码交给BeautifulSoup
        main_page = BeautifulSoup(resp.text, "html.parser")
        # 这里需要自己从网页源码中找需要爬取内容的标签以及class等标识
        alist = main_page.find_all("a", class_="preview")
        if alist == []:
            return 100
        else:
            for a in alist:
                # print(a.get('href'))
                # time.sleep(1)
                href = a.get('href')
                # 拿到子页面源码
                child_page_resp = requests.get(href)
                child_page_resp.encoding = 'utf-8'
                child_page_text = child_page_resp.text
                # 从子页面拿到图片下载路径
                child_page = BeautifulSoup(child_page_text, "html.parser")
                # 这里也需要自己从网页源码中找特殊的那个标签或者class等唯一标识
                div = child_page.find("div", class_="scrollbox")
                # print(div)
                # time.sleep(1)
                img = div.find("img")
                # print(img.get("src"))
                # time.sleep(1)
                src = img.get("src")
                # 下载图片
                img_resp = requests.get(src)
                # 拿到url中最后一个/后面的内容
                img_name = src.split("/")[-1]
                # 如果图片名不存在
                if not os.path.exists("img/Animi/" + img_name):
                    with open("img/Animi/" + img_name, mode="wb")as f:
                        # 图片内容写入文件
                        f.write(img_resp.content)
                        print("finish", img_name)
                        time.sleep(1)
                else:
                    print(img_name + " exists--------------------------")

    except Exception as exc:
        print(str(exc) + ' 4')


# 全取
if __name__ == '__main__':
    try:
        downloadPicP(urlPeople, headers)
        while 1 == 1:
            target = downloadPicsP(headers, countP, urlPeople)
            if target == 100:
                break
            else:
                print("----------------------page {0} People finish------------------------".format(countP))
                countP += 1
        downloadPicA(urlAnimi, headers)
        while 1 == 1:
            target = downloadPicsA(headers, count, urlAnimi)
            if target == 100:
                break
            else:
                print("----------------------page {0} Animi finish------------------------".format(count))
                count += 1

    except Exception as exc:
        print(str(exc) + ' 3')

