"""
GET, POST
取得所有文章: 取得所有資料，輸出結構如下：{ id, url_id, title, date, content}
取得單一文章: 提供id，輸出結構如下：{ id, url_id, title, date, content}
新增: 要提供 title, date(確認是否為日期格式), content； url_id使用/Popular/Detail/＋序號, id自行產生

PUT
修改： 提供id(確認是否是數字), 可修改title or date（確認是否為日期格式） or content

DELETE
刪除: 使用id刪除，提供aip id（確認是否是數字）
"""


from django.shortcuts import render
from .serializers import NewsModelSerializer
from django.http import JsonResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .models import News
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def dailyview_list(request):

    if request.method == 'GET':
        
        news_lst = News.objects.all()
        news_serializer = NewsModelSerializer(news_lst, many=True)
        return JsonResponse(news_serializer.data, safe=False)
 
    elif request.method == 'POST':
        news_data = JSONParser().parse(request)
        news_serializer = NewsModelSerializer(data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def dailyview_detail(request, pk):

    # print('request', request)
    # print('pk', pk)
    try: 
        news_item = News.objects.get(pk=pk) 
    except News.DoesNotExist: 
        return JsonResponse({'message': '熱門新聞沒有此篇文章'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        news_serializer = NewsModelSerializer(news_item) 
        return JsonResponse(news_serializer.data) 
 
    elif request.method == 'PUT': 
        news_data = JSONParser().parse(request) 
        print('news_data', news_data)
        print('news_itme', news_item)
        news_serializer = NewsModelSerializer(news_item, data=news_data, partial=True) 
        if news_serializer.is_valid():
            news_serializer.save() 
            return JsonResponse(news_serializer.data) 
        return JsonResponse(news_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        news_item.delete() 
        return JsonResponse({'message': '此篇文章已被刪除!'}, status=status.HTTP_204_NO_CONTENT)







