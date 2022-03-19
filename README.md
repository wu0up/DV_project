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
，設計4隻api，包含：新增、刪除、修改、取得熱門新聞的文章

### 操作方式
先到http://35.201.189.190/api/token/
取得authentication code

#### 1. 取得熱門新聞的文章
URL: http://35.201.189.190/DailyView/api


