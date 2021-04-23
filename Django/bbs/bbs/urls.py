"""BBS14 URL Configuration

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
from django.views.static import serve
from bbs import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 注册页面
    url(r'^register/', views.register, name='reg'),
    # 登录页面
    url(r'^login/', views.login, name='login'),
    # 图片验证码相关操作
    url(r'^get_code/', views.get_code, name='gc'),
    # 首页
    url(r'^home/', views.home, name='home'),
    # 修改密码
    url(r'^set_password/', views.set_password, name='set_pwd'),
    # 退出登录
    url(r'^logout/', views.logout, name='logout'),
    # 暴露后端指定文件夹资源
    url(r'^media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
    # 在暴露资源的时候一定要明确该资源是否可以暴露
    # url(r'^app01/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT})
    # 点赞点踩
    url(r'^up_or_down/', views.up_or_down),
    # 评论
    url(r'^comment/', views.comment),
    # 后台管理
    url(r'^backend/', views.backend),
    # 添加文章
    url(r'^add/article/', views.add_article),
    # 编辑器上传图片接口
    url(r'^upload_image/', views.upload_image),
    # 修改用户头像
    url(r'^set/avatar/', views.set_avatar),
    # 个人站点页面搭建
    url(r'^(?P<username>\w+)/$', views.site, name='site'),
    # 侧边栏筛选功能
    # url(r'^(?P<username>\w+)/category/(\d+)/',views.site),
    # url(r'^(?P<username>\w+)/tag/(\d+)/',views.site),
    # url(r'^(?P<username>\w+)/archive/(\w+)/',views.site),
    # 上面的三条url其实可以合并成一条
    url(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/', views.site),
    # 文章详情页
    url(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/', views.article_detail),

]
