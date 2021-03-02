from django.db import models

# Create your models here.


class User(models.Model):
    # id int primary_key auto_increment
    id = models.AutoField(primary_key=True, verbose_name="主键")
    # username varchar(32)
    username = models.CharField(max_length=32, verbose_name="用户名")
    """
    CharField必须要指定max_length参数，不写会报错
    verbose_name该参数是所有字段都有的，就是用来对字段的解释
    """
    # password int
    # password = models.IntegerField(verbose_name="密码")
    password = models.CharField(verbose_name="密码", max_length=64)
    # 新增字段
    age = models.IntegerField(verbose_name='年龄', default=0)
    # 注释掉即删除该字段
    # info = models.CharField(max_length=32, verbose_name='个人简介', null=True)
    # hobby = models.CharField(max_length=32, verbose_name='兴趣爱好', default='study')


class Author(models.Model):
    # 由于一张表中必须要有一个主键字段，并且一般情况下都叫id字段，
    # 所以orm当你不定义主键id字段的时候，orm会自动帮你创建一个名为id的主键字段
    # username varchar(32)
    username = models.CharField(max_length=32)
    # password int
    password = models.IntegerField()