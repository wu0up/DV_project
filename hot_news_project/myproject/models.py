from django.db import models
from datetime import datetime

# create the hot_news
class  News(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    url_id = models.CharField(max_length=30, verbose_name='網址', default='')
    title = models.CharField(max_length=200, verbose_name='標題', default='')
    date = models.DateField(verbose_name ='日期')
    content = models.TextField(verbose_name='內文')

    class Meta:  #表單名稱
        verbose_name = '熱門新聞'
        verbose_name_plural = verbose_name

    
