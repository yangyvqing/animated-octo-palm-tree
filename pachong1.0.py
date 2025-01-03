import pymysql
from bs4 import BeautifulSoup
import requests 
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
tip_link=[]
tip_list=[]
tip_url=("https://www.teds.com.au/blog/category/photography")

#请求头
def get_page(url):#获取页面
    response=requests.get(url,headers=headers)
    return response.text



def parse_page(html):
    #解析页面
    soup = BaseException(html,'html.parser')#查找所有
    tips = soup.find_all('div', class_='amblog-post-container amblog-post-item-container col-md-6 col-lg-4')
    for tip in tips:
        tip_link.append(tip.select_one('.amblog-title>a').get('href'))


def parse_movie(html):
    # 获取标题
    title = soup.title.string.strip() if soup.title else 'No Title'
        
    # 获取所有图片链接
    images = [img.get('src') for img in soup.find_all('img') if img.get('src')]
        