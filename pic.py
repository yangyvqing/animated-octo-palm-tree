import requests
from bs4 import BeautifulSoup

# 获取网页标题和图片
def get_subpage_content(url):
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        if response.status_code != 200:
            print(f'Failed to retrieve {url}')
            return None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取标题
        title = soup.title.string.strip() if soup.title else 'No Title'
        
        # 获取所有图片链接
        images = [img.get('src') for img in soup.find_all('img') if img.get('src')]
        
        return title, images
    except Exception as e:
        print(f'Error fetching {url}: {e}')
        return None

# 从一级页面获取二级页面链接
def get_subpage_links(url):
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        if response.status_code != 200:
            print(f'Failed to retrieve {url}')
            return []
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 根据实际情况选择合适的选择器获取二级链接
        subpage_links = [a.get('href') for a in soup.find_all('a') if 'page' in a.get('href', '')]  # 这里的 'page' 是示例，你可以根据需要调整
        
        return subpage_links
    except Exception as e:
        print(f'Error fetching {url}: {e}')
        return []

# 主程序
if __name__ == '__main__':
    base_url = 'https://example.com/category'  # 替换为你要获取的一级页面的URL
    subpages = get_subpage_links(base_url)
    
    for subpage in subpages:
        title, images = get_subpage_content(subpage)
        if title and images:
            print(f'Title: {title}')
            print('Images:')
            for img in images:
                print(img)
            print('---')  # 分隔每个子页面的输出