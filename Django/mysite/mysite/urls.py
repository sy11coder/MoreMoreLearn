"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 写我们自己的路由与视图函数对应关系
    url(r'^index/', views.index),
    url(r'home/', views.home),
    # 登陆功能
    url(r'^login/', views.login),
    # 注册功能
    url(r'^register', views.reg),
    # 展示用户列表
    url(r'^userlist/', views.userlist),
    # 编辑用户
    url(r'^edit_user/', views.edit_user),
    # 删除用户
    url(r'^delete_user/', views.delete_user)
]
