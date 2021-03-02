from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def home(request):
    return HttpResponse('HOME')


def delete_user(request):
    # 获取用户想要删除的数据id值
    delete_id = request.GET.get('user_id')
    # 直接去数据库中找到对应的数据删除即可, 批量删除
    models.User.objects.filter(id=delete_id).delete()
    # 跳转到数据展示的页面
    return redirect('/userlist/')


def edit_user(request):
    # 获取url问号后面的参数
    edit_id = request.GET.get('user_id')
    # 查询当前用户想要编辑的数据对象
    edit_obj = models.User.objects.filter(id=edit_id).first()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库中修改对应的数据内容
        # # 修改数据方式1, 将filter查询出来的列表中的所有对象全部更新，批量操作更新,只修改被修改的字段
        # models.User.objects.filter(id=edit_id).update(username=username, password=password)
        # 修改数据方式2,字段特别多的时候，效率会非常的低(从头到尾将数据的所有字段全部更新一遍，无论该字段是否被修改)
        edit_obj.username = username
        edit_obj.password = password
        edit_obj.save()
        # 跳转到数据展示的页面
        return redirect('/userlist/')
    # 将数据对象展示到页面上
    return render(request, "edit_user.html", locals())


def userlist(request):
    # 查询出用户表里面所有的数据
    # # 方式一
    # data = models.User.objects.filter()
    # print(data)
    # 方式二
    user_queryset = models.User.objects.all()
    # return render(request, 'userlist.html', {'user_queryset': user_queryset})
    return render(request, 'userlist.html', locals())


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # # 直接获取用户数据存入数据库
        # res = models.User.objects.create(username=username, password=password)
        # # 返回值就是当前被创键的对象本身
        # print(res, res.username, res.password)

        user_obj = models.User(username=username, password=password)
        user_obj.save()  # 保存数据
    # 先给用户返回一个注册页面
    return render(request, 'reg.html')


def login(request):
    # 返回一个登陆界面
    """
    get请求和post请求应该有不同的处理机制
    :param request: 请求相关的数据对象， 里面有很多简易的方法
    :return:
    """
    print(request.method)
    if request.method == "POST":
        # # 获取前端用户提交的post请求数据(不包含文件)
        # print(request.POST)   # < QueryDict: {'username': ['23'], 'password': ['2332']} >
        # username = request.POST.get('username')  # get只会获取列表最后一个元素
        # print(username, type(username))
        # password = request.POST.getlist('password')  # getlist会获取列表
        # print(password, type(password))

        # 获取用户的用户名和密码， 然后利用orm操作数据，校验数据是否正确
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去数据库中查询数据
        user_obj = models.User.objects.filter(username=username).first()
        # select * from user where username='jason';
        # <QuerySet [<User: User object (1)>]> [数据对象1，数据对象2...]
        # user_obj = res[0]
        # print(user_obj)
        # print(user_obj.username)
        # print(user_obj.password)
        if user_obj:
            # 比对密码是否一致
            if password == user_obj.password:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse("用户不存在")
    return render(request, 'login.html')


def index(request):
    """
    :param request: 请求相关的所有数据对象
    :return:
    """
    user_dict = {'username': 'jason', 'age': 18}
    # return HttpResponse("你好啊")
    # return render(request, 'myfirst.html', {'data': user_dict})   # 自动去templates文件夹帮你查找文件，指定要传递的
    return render(request, 'myfirst.html', locals())  # locals会将所在的名称空间中所有的名字全部传递给html页面
    # return redirect('https://baidu.com')
    # return redirect('/home/')
