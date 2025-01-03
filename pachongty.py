import requests
from bs4 import BeautifulSoup

def get_subpage_content(url):
    # 发送请求并获取页面内容
    response = requests.get(url)
    response.encoding = response.apparent_encoding  # 确保正确编码
    if response.status_code != 200:
        print(f'Failed to retrieve {url}')
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 获取标题
    title = soup.title.string if soup.title else 'No Title'
    
    # 获取图片链接
    images = []
    for img in soup.find_all('img'):
        img_src = img.get('src')
        if img_src:
            images.append(img_src)
    
    return title, images

# 示例使用
url = 'https://www.teds.com.au/blog/category/photography'  # 替换为你的目标网址
title, images = get_subpage_content(url)

print(f'Title: {title}')
print('Images:')
for img in images:
    print(img)