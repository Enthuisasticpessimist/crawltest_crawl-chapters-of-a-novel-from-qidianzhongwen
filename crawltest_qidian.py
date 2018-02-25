from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


head_url = "http:"
tail_url = "//read.qidian.com/chapter/XB-t-t4woPprP-ysb_RHlg2/avg4RS7mH_JOBDFlr9quQA2"

while True:
    url = head_url+tail_url

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')

    chapter_name = soup.find("h3",{"class":"j_chapterName"}).get_text()
    chapter_content = soup.find_all("div",
                        {"class":"read-content j_readContent"})
    tail_url = soup.find("a",{"id":"j_chapterNext"})['href']



    with open("Menshenxingtu.txt","a") as f:
        f.write(chapter_name)
        for child in chapter_content:
            f.write(child.get_text()+'\n')



