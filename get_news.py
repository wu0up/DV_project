import sys
#sys.path.append("/usr/local/lib/python3.7/site-packages")
import requests
import psycopg2
from bs4 import BeautifulSoup
import re


res = requests.get('https://dailyview.tw')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

url_lst=[]
#取得url list
for news in soup.select('.fav_block'):
    a = news['href']
    url_lst.append(a)


def insert_table(id_no, url, title, date, content):
    conn = psycopg2.connect(host="35.189.186.47", user="postgres", password="abcd1234", database="postgres") 
    cur = conn.cursor() 
    # last_insert_id = None # inserting data in users table 
    sql_query = "insert into myproject_news (id, url_id, title, date, content) values (%s, %s, %s, %s, %s);" 
    sql_data = (id_no, url, title, date, content) 
    cur.execute(sql_query, sql_data) 
    conn.commit() 
    cur.close() 
    conn.close() 

def get_url_id():
    conn = psycopg2.connect(host="35.189.186.47", user="postgres", password="abcd1234", database="postgres") 
    cur = conn.cursor() 
    sql_query = "SELECT url_id FROM myproject_news;" 
    cur.execute(sql_query) 
    mobile_records = [i[0] for i in cur.fetchall()]
    return mobile_records

p = re.compile('/Popular/')
url_lst_edit = [ s for s in url_lst if p.match(s) ]
url_lst_edit =list(set(url_lst_edit))
saved_lst = get_url_id()
url_lst_final = [x for x in url_lst_edit if x not in saved_lst]


for url in url_lst_final:
    link = 'https://dailyview.tw'+url
    print(link)
    id_no =url_lst_final.index(url)
    res = requests.get(link)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    title = soup.select('h1')[0].text
    time_content = soup.select('.time')
    if len(time_content)>=1:
        time =time_content[0].text
    else:
        time = soup.select('time')[0].text
    print(time)
    #content = soup.select('.main_article')[0]
    contents = soup.find_all('p',{'dir': 'ltr'})
    all_content =[]
    for i in contents:
        all_content.append(i.text)
    content = ' '.join(all_content)
  
    insert_table(id_no, url, title, time, content)

