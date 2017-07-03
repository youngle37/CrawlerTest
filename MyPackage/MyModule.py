
# coding: utf-8

# In[ ]:

import os
import requests
import shutil

from bs4 import BeautifulSoup

sci = "https://www.scientificamerican.com"
files_path = "~/60s"

def download(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    
    title = soup.select("#sa_body > header > div.article-header__inner.tooltip-outer > h3")[0].string
    
    script = soup.select("#sa_body > div.article-grid-outer.podcast-grid-outer.container > div > section > div.transcript > div.transcript__inner")[0].text
    script = script[:script.rfind('\n')]
    
    download_link = sci + soup.select("#sa_body > header > div.podcasts-media.podcasts-media--feature.podcasts__media > div > a")[0]['href']
    
    os.makedirs(os.path.join(os.path.expanduser(files_path), title))
    
    path = os.path.join(os.path.expanduser(files_path), title)
    
    fname_mp3 = os.path.join(path, title+".mp3")
    fname_script = os.path.join(path, title+".txt")
    
    print title
    
    file_download(fname_mp3, download_link)
    script_download(fname_script, script)
    
    
def find_page_num(url):
    url = url + "1"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    
    page_num = soup.select("#sa_body > div.landing-main > section > div.videos__btn > footer > div.pagination__main > ol > li > a")[-1].string
    return int(page_num)

def download_main(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    
    link = soup.select("#sa_body > div.landing-main > div.podcasts.container > div.podcasts-header.podcasts-header--feature.tooltip-outer > h3 > a")[0]['href']
    download(link)
    
def download_link(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html5lib")
    
    all_link = soup.select("#sa_body > div.landing-main > section > div > section > div.podcasts-listing__main > h3 > a")
    for link in all_link:
        download(link['href'])
    
def file_download(fname, link):
    res = requests.get(link, stream=True)
    f = open(fname, 'wb')
    shutil.copyfileobj(res.raw, f)
    f.close()
    
def script_download(fname, script):
    f = open(fname, 'w')
    f.write(script.encode('utf-8'))
    f.close()

