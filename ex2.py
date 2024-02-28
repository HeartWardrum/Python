import requests
from bs4 import BeautifulSoup
import openpyxl

# 定义搜索关键词和搜索引擎URL
search_query = "python3执行google搜索"
search_url = f"https://www.google.com/search?q=python3%E6%89%A7%E8%A1%8Cgoogle%E6%90%9C%E7%B4%A2&newwindow=1&sca_esv=7fcd6f03a496d01d&ei=VOXeZevzLJXbkPIP9ceR0AM&ved=0ahUKEwjr7cD2xc2EAxWVLUQIHfVjBDoQ4dUDCBA&uact=5&oq=python3%E6%89%A7%E8%A1%8Cgoogle%E6%90%9C%E7%B4%A2&gs_lp=Egxnd3Mtd2l6LXNlcnAiGXB5dGhvbjPmiafooYxnb29nbGXmkJzntKIyCBAAGIkFGKIEMggQABiABBiiBDIIEAAYgAQYogRI9FdQ9htY5FZwAXgBkAEAmAHNBKABxUiqAQoyLTEuMjMuMi4xuAEDyAEA-AEBmAIZoAKCQcICChAAGEcY1gQYsAPCAgUQABiABJgDAIgGAZAGCpIHCDEuMy0yMS4z&sclient=gws-wiz-serp"

# 发送HTTP请求获取搜索结果页面
response = requests.get(search_url)
soup = BeautifulSoup(response.text, "html.parser")

# 提取搜索结果标题
results = soup.find_all(
    "h3", class_="t"
)  # Google搜索结果的标题通常在<h3>标签中，class为't'
titles = [result.text for result in results]

# 将搜索结果写入Excel文件
workbook = openpyxl.Workbook()
sheet = workbook.active

# 写入标题行
sheet["A1"] = "搜索结果"

# 写入搜索结果
for i, title in enumerate(titles, start=2):
    sheet[f"A{i}"] = title

# 保存Excel文件
workbook.save("搜索结果.xlsx")
