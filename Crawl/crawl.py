from bs4 import BeautifulSoup
import requests
import json

def crawl_data(url):
    result = [] # chưa dùng
    news_dict = {}
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/80.0.180 Chrome/74.0.3729.180 Safari/537.36'}
    req = requests.get(url, headers = headers, verify = False)
    

    soup = BeautifulSoup(req.text, "lxml")
    title_news = soup.find('h1', {'class':'entry-title'})
    news_content = soup.find("div", {'class': 'td-post-content'})
    p = news_content.find_all('p')
    
    news_content = ' '.join(item.text for item in p)
    # print(content)
    # news_content = content.encode('utf-8', 'replace')

    news_dict['title'] = title_news.text
    news_dict['content'] = news_content
    
    return news_dict
    
#crawl demo
url = "http://hoicodo.com/2019/07/182922/khoi-hai-lu-ban-nuoc-lai-di-day-nguoi-khac-giu-nuoc-the-nao/"
cr = crawl_data(url)
print(cr)

with open("kompas.json","w") as f:
    json.dump(cr, f)
with open("kompas.json", 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    x = data['content']
    



