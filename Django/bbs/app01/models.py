"""
由于django自带的sqlite数据库对日期不敏感，所以我们换成MySQL
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.BigIntegerField(verbose_name='手机号', null=True, blank=True)
    """
       null=True   数据库该字段可以为空
       blank=True  admin后台管理该字段可以为空
    """
    # 头像
    avatar = models.FileField(upload_to='avatar/', default='avatar/default.png', verbose_name='用户头像')
    """
    给avatar字段传文件对象 该文件会自动存储到avatar文件下 然后avatar字段只保存文件路径avatar/default.png
    """
    create_time = models.DateField(auto_now_add=True)

    blog = models.OneToOneField(to='Blog', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name_plural = '用户表'  # 修改admin后台管理默认的表名
        # verbose_name = '用户表'  # 末尾还是会自动加s

    def __str__(self):
        return self.username


class Blog(models.Model):
    site_name = models.CharField(verbose_name='站点名称', max_length=32)
    site_title = models.CharField(verbose_name='站点标题', max_length=32)
    # 简单模拟 带你认识样式内部原理的操作
    site_theme = models.CharField(verbose_name='站点样式', max_length=64)  # 存css/js的文件路径

    def __str__(self):
        return self.site_name


class Category(models.Model):
    name = models.CharField(verbose_name='文章分类', max_length=32)
    blog = models.ForeignKey(to='Blog', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name='文章标签', max_length=32)
    blog = models.ForeignKey(to='Blog', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(verbose_name='文章标题', max_length=64)
    desc = models.CharField(verbose_name='文章简介', max_length=255)
    # 文章内容有很多 一般情况下都是使用TextField
    content = models.TextField(verbose_name='文章内容')
    create_time = models.DateField(auto_now_add=True)

    # 数据库字段设计优化
    up_num = models.BigIntegerField(verbose_name='点赞数', default=0)
    down_num = models.BigIntegerField(verbose_name='点踩数', default=0)
    comment_num = models.BigIntegerField(verbose_name='评论数', default=0)

    # 外键字段
    blog = models.ForeignKey(to='Blog', on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING, null=True)
    tags = models.ManyToManyField(to='Tag',
                                  through='Article2Tag',
                                  through_fields=('article', 'tag')
                                  )

    def __str__(self):
        return self.title


class Article2Tag(models.Model):
    article = models.ForeignKey(to='Article', on_delete=models.DO_NOTHING)
    tag = models.ForeignKey(to='Tag', on_delete=models.DO_NOTHING)


class UpAndDown(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.DO_NOTHING)
    article = models.ForeignKey(to='Article', on_delete=models.DO_NOTHING)
    is_up = models.BooleanField()  # 传布尔值 存0/1


class Comment(models.Model):
    user = models.ForeignKey(to='UserInfo', on_delete=models.DO_NOTHING)
    article = models.ForeignKey(to='Article', on_delete=models.DO_NOTHING)
    content = models.CharField(verbose_name='评论内容', max_length=255)
    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    # 自关联 # 有些评论就是根评论
    parent = models.ForeignKey(to='self', on_delete=models.DO_NOTHING, null=True)
