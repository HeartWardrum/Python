import requests
from bs4 import BeautifulSoup

# 发起HTTP请求
url = "https://www.google.com/search?q=python3%E6%89%A7%E8%A1%8Cgoogle%E6%90%9C%E7%B4%A2&newwindow=1&sca_esv=7fcd6f03a496d01d&ei=VOXeZevzLJXbkPIP9ceR0AM&ved=0ahUKEwjr7cD2xc2EAxWVLUQIHfVjBDoQ4dUDCBA&uact=5&oq=python3%E6%89%A7%E8%A1%8Cgoogle%E6%90%9C%E7%B4%A2&gs_lp=Egxnd3Mtd2l6LXNlcnAiGXB5dGhvbjPmiafooYxnb29nbGXmkJzntKIyCBAAGIkFGKIEMggQABiABBiiBDIIEAAYgAQYogRI9FdQ9htY5FZwAXgBkAEAmAHNBKABxUiqAQoyLTEuMjMuMi4xuAEDyAEA-AEBmAIZoAKCQcICChAAGEcY1gQYsAPCAgUQABiABJgDAIgGAZAGCpIHCDEuMy0yMS4z&sclient=gws-wiz-serp"
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, "html.parser")

    # 检查是否存在<title>标签
    title_tag = soup.title
    if title_tag:
        title = title_tag.text
        print(f"网页标题：{title}")
    else:
        print("页面没有<title>标签")
    # 提取所有链接
    # links = soup.find_all("a")
    # for link in links:
    #     print(f"链接：{link['href']}")
else:
    print(f"请求失败，状态码:{response.status_code}")
