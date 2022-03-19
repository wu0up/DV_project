# 管理API Django Project
使用docker-compose 將api部署在GCP VM

### Package
- python 3.7
- PostgreSQL (Google SQL)
- Django 3.2
- Nginx
- uWSGI

### 需求
針對網站（https://dailyview.tw/）
，設計4隻api，包含：新增、刪除、修改、取得熱門新聞的文章；<br>

### 使用資料
使用熱門文章區塊中標記'/Popular/'的資料，<br>
資料表欄位：url_id(部分url, "/Popular/Detail/13708"), title（標題), date(文章發布日期）, content(文章內容）<br>
資料是使用get_news.py從https://dailyview.tw/爬下來後，存到table-myproject_news<br>

### 操作方式
先到http://35.201.189.190/api/token/
取得access code，
作為Authorization的值
```python
headers = {
  'Authorization': 'Bearer+access code'
}
```

#### 1. 取得熱門新聞的文章
- 取得所有文章
URL: http://35.201.189.190/DailyView/api <br>
method: GET <br>
![image](https://github.com/wu0up/DV_project/blob/main/image/get.png)<br>

- 取得個別文章
URL: http://35.201.189.190/DailyView/api/id <br>
method: GET <br>
![image](https://github.com/wu0up/DV_project/blob/main/image/get_1.png)<br>

#### 2. 新增熱門新聞的文章
URL: http://35.201.189.190/DailyView/api <br>
method: POST <br>
格式：
```python
{
   "url_id": ,
   "title": ,
   "date": ,
   "content": 
}
```
![image](https://github.com/wu0up/DV_project/blob/main/image/post.png)<br>

#### 3. 修改熱門新聞的文章
URL: http://35.201.189.190/DailyView/api/id <br>
method: PUT <br>
格式(可修改單個或多個欄位）：
```python
{
   "title":
}
```
![image](https://github.com/wu0up/DV_project/blob/main/image/put.png)<br>

#### 4. 刪除熱門新聞的文章
URL: http://35.201.189.190/DailyView/api/id <br>
method: DELETE <br>

![image](https://github.com/wu0up/DV_project/blob/main/image/Delete.png)<br>


