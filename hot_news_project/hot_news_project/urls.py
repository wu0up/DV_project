""""
routes:

/DailyView/api/: GET, POST
/DailyView/api/:id: GET, PUT, DELETE

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from myproject import views
#from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('jwt_token/', obtain_jwt_token),     # 獲取token，登入檢視
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^DailyView/api$', views.dailyview_list),
    url(r'^DailyView/api/(?P<pk>[0-9]+)$', views.dailyview_detail)
]
