from bs4 import BeautifulSoup
import requests 
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
for start_num in range(0,250,25):
    content=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    html= content.text
    soup=BeautifulSoup(html,"html.parser")
    all_titles = soup.find_all("span",attrs={"class":"title"})
    for title in all_titles:
        title_string=(title.string)
        if"/" not in title_string:
            print(title_string)