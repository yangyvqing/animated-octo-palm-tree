import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
import re
import time  # 用于添加延迟

# 数据库配置
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# 创建数据库连接
def create_connection():
    """
    创建并返回一个MySQL数据库连接对象。
    """
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to MySQL database")
    except Error as e:
        print(f"Error: {e}")
    return connection

# 创建表
def create_table(connection):
    """
    在数据库中创建一个名为`articles`的表。
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT,
                image_url VARCHAR(255)
            )
        """)
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

# 插入数据
def insert_article(connection, title, content, image_url):
    """
    将文章数据插入到数据库的`articles`表中。
    """
    try:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO articles (title, content, image_url)
            VALUES (%s, %s, %s)
        """, (title, content, image_url))
        connection.commit()
        print(f"Inserted article: {title}")
    except Error as e:
        print(f"Error: {e}")

# 获取文章内容
def get_article_content(url):
    """
    从指定URL的文章页面中提取标题、正文和图片URL。
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)  # 添加请求头
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 获取标题
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No Title'
        
        # 获取正文
        content = ''
        for paragraph in soup.find_all('p'):
            content += paragraph.get_text(strip=True) + '\n'
        
        # 获取图片
        image = soup.find('img')
        image_url = image['src'] if image else 'No Image'
        
        return title, content, image_url
    except Exception as e:
        print(f"Error fetching content from {url}: {e}")
        return None, None, None

# 主函数
def main():
    """
    主函数，负责协调整个爬虫程序的运行。
    """
    base_url = 'https://www.teds.com.au/blog/category/photography'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        response = requests.get(base_url, headers=headers)  # 添加请求头
        response.raise_for_status()  # 检查请求是否成功
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 获取所有文章链接
        article_links = []
        for article in soup.find_all('a', href=re.compile(r'/blog/photography/')):  # 使用正则表达式匹配链接
            link = article['href']
            if link not in article_links:
                article_links.append(link)
        
        print(f"Found {len(article_links)} articles to scrape.")
        
        # 连接数据库
        connection = create_connection()
        if connection:
            create_table(connection)
            
            # 遍历文章链接并插入数据库
            for link in article_links:
                full_url = f"https://www.teds.com.au{link}"  # 拼接完整URL
                print(f"Scraping {full_url}...")
                title, content, image_url = get_article_content(full_url)
                if title and content:  # 确保数据有效
                    insert_article(connection, title, content, image_url)
                time.sleep(2)  # 添加延迟，避免频繁请求
        
            # 关闭数据库连接
            connection.close()
            print("Database connection closed")
    except Exception as e:
        print(f"Error in main function: {e}")

# 程序入口
if __name__ == "__main__":
    main()