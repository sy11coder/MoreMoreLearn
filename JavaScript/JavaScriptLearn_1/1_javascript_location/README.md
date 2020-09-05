1、内部js放在\<script>\</script>标签中

2、外部js通过src属性引入：\<script src="javascript.js">\</script>

3、一旦\<script src="javascript.js">\</script>标签已引入外部js，该标签不能再编写内部js，即使编写了也会被浏览器忽略。但是可以重新再写一个\<script>\</script>用于放内部js

4、外部js可以在不同页面中同时引用，也可以利用到浏览器的缓存机制，相比于内部js更易维护

5、js代码可写到onclick属性中，当我们点击按钮时，会执行js代码

6、js代码也可写到href属性中，这样当点击超链接时，会执行js代码

7、alert("弹出内容")

8、document.write("内容输出显示在body标签中")
        
9、console.log("内容输出显示在控制台中")

10、https://www.bilibili.com/video/av30099487/?p=18

11、https://www.bilibili.com/video/av30099487/?p=16