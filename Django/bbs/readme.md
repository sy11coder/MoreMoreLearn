# 今日概要

```python
"""
1.简述自定义标签，过滤器，inclusion_tag的方法，并简要说一说三者的特点及响应流程
2.简述个人侧边栏展示及筛选业务逻辑
3.简述点赞点踩业务逻辑(前后端分开描述)
4.简述根评论业务逻辑(前后端分开描述)
"""
```

# 其它内容

* 侧边栏制作inclusion_tag

  ```python
  """
  1.当一个页面的局部需要再多个页面使用并且还需要传参数
  
  自定义inclusion_tag步骤
  	1.在应用下创建名字必须叫templatetags文件夹
  	2.文件夹内创建任意名称的py文件
  	3.py文件内先书写固定的两行代码
  	from django import template
  	register = template.Library()
  	
  	@register.inclusion_tag(left_menu.html)
  	def index():
  		准备上述页面需要的数据
  		return locals()
  """
  ```

* 点赞点踩

  ```python
  # 前端页面
  	1.拷贝博客园点赞点踩前端样式
    	html代码 + css代码
    2.如何判断用户到底点击了哪个图标
    	恰巧页面上只有两个图标，所以给两个图标标签添加一个公共的样式类
      然后给这个样式类绑定点击事件
      再利用this指代的就是当前被操作对象 利用hasClass判断是否有某个特定的类属性，从而判断出到底是两个图标中的哪一个
    3.书写ajax代码朝后端提交数据
    
    4.后端逻辑书写完毕之后 前端针对点赞点踩动作实现需要动态展示提示信息
    		1.前端点赞点踩数字自增1 需要注意数据类型的问题
      		Number(old_num) + 1
        2.用户没有登陆 需要展示没有登陆提示 并且登陆可以点击跳转
        	html()
          |safe
          mark_safe()
  # 后端逻辑
  	1.先判断用户是否登陆
    	request.user.authenticated()
    2.再判断当前文字是否是当前用户自己写的
    	通过文章主键值获取文章对象
      之后利用orm查询获取文章对象对应的用户对象与request.user比对
   	3.判断当前用户是否已经给当前文章点了
    	利用article_obj文章对象和request.user用户对象去点赞点踩表中筛选数据如果有数据则点过没有则没点
    4.操作数据库	需要注意要同时操作两张表
    	# 前端发送过来的是否点赞是一个字符串 需要你自己转成布尔值或者用字符串判断
      is_up = json.loads(is_up)
      F模块
   """
   总结:在书写较为复杂的业务逻辑的时候，可以先按照一条线书写下去
   之后再去弥补其他线路情况
   	类似于先走树的主干 之后再分散
   """
  ```

* 评论

  ```python
  # 先写根评论
  	先吧整体的评论功能跑通 再去填补
    1.书写前端获取用户评论的标签
    	可能点赞点踩有浮动带来的影响
      	clearfix
    2.点击评论按钮发送ajax请求
    
    3.后端针对评论单独开设url处理
    	后端逻辑其实非常的简单非常的少
      
    4.针对根评论涉及到前端的两种渲染方式
    	1.DOM操作临时渲染评论楼
      	需要用到模版字符串
        	// 临时渲染评论楼
                          let userName = '{{ request.user.username }}';
                          let temp = `
                          <li class="list-group-item">
  
                              <span>${userName}</span>
                              <span><a href="#" class="pull-right">回复</a></span>
                              <div>
                                  ${conTent}
                              </div>
                              </li>
                          `
                          // 将生成好的标签添加到ul标签内
                          $('.list-group').append(temp);
      2.页面刷新永久(render)渲染
      	后端直接获取当前文章对应的所有评论 传递给html页面即可
        前端利用for循环参考博客园评论楼样式渲染评论
        
      3.评论框里面的内容需要清空
  # 再考虑子评论
  	从回复按钮入手
    	点击回复按钮发生了哪些事
      	1.评论框自动聚焦	.focus()
       	2.评论框里面自动添加对应评论的评论人姓名
        	@username\n
      思考:
        	1.根评论和子评论点的是同一个按钮
        	2.根评论和子评论的区别
          	其实之前的ajax代码只需要添加一个父评论id即可
      
      点击回复按钮之后 我们应该获取到根评论对应的用户名和主键值
      针对主键值 多个函数都需要用 所以用全局变量的形式存储
      
      针对子评论内容 需要切割出不是用户写的	@username\n
      				// 获取用户评论的内容
              let conTent = $('#id_comment').val();
              // 判断当前评论是否是子评论 如果是 需要将我们之前手动渲染的@username去除
              if(parentId){
                  // 找到\n对应的索引 然后利用切片 但是前片顾头不顾尾 所以索引+1
                  let indexNum = conTent.indexOf('\n') + 1;
                  conTent = conTent.slice(indexNum)  // 将indexNum之前的所有数据切除 只保留后面的部分
              }
      
      后端parent字段本来就可以为空，所以传不传值都可以直接存储数据
      
  		前端针对子评论再渲染评论楼的时候需要额外的判断
      	{% if comment.parent_id %}
             <p>@{{ comment.parent.user.username }}</p>
        {% endif %}
             {{ comment.content }}
      前端parentId字段每次提交之后需要手动清空  
  ```

# 内容概要

* 后台管理

  文章查增		改删

  前端编辑器(kindeditor富文本编辑器)

  处理XSS攻击以及文章摘要的处理

* 编辑器上传图片

* 修改用户头像

* bbs小总结

* 后期建议(聊一聊)

# 内容详细

### 后台管理

```python
"""
当一个文件夹下文件比较多的时候 你还可以继续创建文件夹分类处理
	templates文件夹
		backend文件夹
		应用1文件夹
		应用2文件夹
"""
```

### 添加文章

```python
有两个需要注意的问题
	1.文章的简介
  	不能直接切去
    	应该先想办法获取到当前页面的文本内容之后截取150个文本字符
  
  2.XSS攻击
  	针对支持用户直接编写html代码的网址
    针对用户直接书写的script标签 我们需要处理
    	1.注视标签内部的内容
      2.直接将script删除

如何解决？
	我们自己的话
  	针对1 后端通过正则表达式筛选
    针对2 首先需要确定及获取script标签
  这两步都好烦 有木有人来帮我一下
  	beautifulsoup模块			bs4模块
    	专门用来帮你处理html页面内的
      该模块主要用于爬虫程序
   
  下载千万不要下错了
  	pip3 install beautifulsoup4
				# 模块使用
        soup = BeautifulSoup(content,'html.parser')

        tags = soup.find_all()
        # 获取所有的标签
        for tag in tags:
            # print(tag.name)  # 获取页面所有的标签
            # 针对script标签 直接删除
            if tag.name == 'script':
                # 删除标签
                tag.decompose()
        # 文章简介
        # 1 先简单暴力的直接切去content 150个字符
        # desc = content[0:150]
        # 2 截取文本150个
        desc = soup.text[0:150]
"""
当你发现一个数据处理起来不是很方便的时候 
可以考虑百度搜搜有没有现成的模块帮你完成相应的功能
"""
```

### kindeditor富文本编辑器

```python
编辑器的种类有很多，你可以自己去网上搜索
```

### 编辑器上传图片

```python
别人写好了接口 但是接口不是你自己的
你需要手动去修改

# 在使用别人的框架或者模块的时候 出现了问题不要慌 看看文档可能会有对应的处理方法
```

### 修改用户头像

```python
@login_required
def set_avatar(request):
    if request.method == 'POST':
        file_obj = request.FILES.get('avatar')
        # models.UserInfo.objects.filter(pk=request.user.pk).update(avatar=file_obj)  # 不会再自动加avatar前缀
        # 1.自己手动加前缀
        # 2.换一种更新方式
        user_obj = request.user
        user_obj.avatar = file_obj
        user_obj.save()
        return redirect('/home/')
    blog = request.user.blog
    username = request.user.username
    return render(request,'set_avatar.html',locals())
```

### bbs项目总结

```python
"""
在开发任意的web项目的时候 其实到了后期需要写的代码会越来越少
都是用已经写好的url填写到a标签href属性完成跳转即可
"""
主要功能总结
	表设计	开发流程(粗燥流程 还可以细化)
  注册功能
  	forms组件使用
    头像动态展示
    错误信息提示
  登陆功能
  	图片验证码
    滑动验证码
  首页展示
  	media配置
    主动暴露任意资源接口
  个人站点展示
  	侧边栏展示
    侧边栏筛选
    侧边栏inclusion_tag
  文章详情页
  	点赞点踩
    评论
  后台管理
"""
针对bbs需要你掌握每一个功能的书写思路 内部逻辑
之后再去敲代码熟悉 找感觉
"""
```

















