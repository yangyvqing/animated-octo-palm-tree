import requests
headers={"Uers-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
response=requests.get("https://www.ormsdirect.co.za/blogs/digital-photography")
if response.ok:
    print(response.text)
else:
    print("请求失败")
