1、字符串在底层是以字符串数组的形式保存的

2、charAt()可以根据索引返回字符串指定位置的字符，与[]一致；

3、charCodeAt()获取指定位置字符编码，返回unicode编码；

4、String.fromCharCode()根据字符编码获取字符

5、concat()可以用来连接两个或多个字符串

6、indexOf()该方法可以检索一个字符串是否含有指定内容,返回其第一次出现的索引， 找不到则返回-1；第二个参数指定开始查找位置

7、lastIndexOf()与indexOf()一致，不同的是它从后面往前找

8、slice(index, index)可以从字符串中截取指定的内容，包括开始位置索引，不包括结束位置索引；省略第二个参数就会截取第一个到后面所有，也可以用负参数

9、substring(index, index)可以用来截取一个字符串，与slice()类似；但是不能接收负值作为参数，并自动调整参数位置

10、substr(index, num)截取字符串，截取开始索引以及要截取的长度

11、split()将字符串拆分成数组

12、toUpperCase()大写，toLowerCase()小写






