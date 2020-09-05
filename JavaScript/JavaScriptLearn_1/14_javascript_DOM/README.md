1、DOM:Document Object Model 文档、对象、模型

2、JS通过DOM来对HTML文档操作，只要理解了DOM就可以随心所欲的操作WEB页面

3、浏览器已经为我们提供文档节点对象，这个对象就是window属性，可以在页面中直接使用，文档节点代表的是整个网页

4、事件：就是用户和浏览器之间的交互行为，比如：点击按钮，鼠标移动，关闭窗口

5、我们可以在事件对应的属性中设置一些js代码，这样当事件被触发时，这些代码将会执行

6、浏览器在加载一个页面时，是按照自上而下的顺序执行的，读一行运行一行

7、onload事件会在整个页面加载完成后，再执行

8、通过document对象调用，获取元素节点

9、getElementById()通过id属性

10、getElementsByTagName()通过标签名

11、getElementsByName()通过name属性

12、innerHTML通过这个属性可以获取到元素内部的html代码

13、如果读取元素节点属性，直接使用元素.属性名；如元素.id；元素.name；元素.className

14、获取元素节点的子节点：通过具体的元素节点调用

15、getElementsByTagName()方法：返回当前节点的指定标签名后代节点

16、childNodes属性，表示当前节点的所有子节点;会获取包括元素节点以及文本节点；包括空白文本

17、firstChild、lastChild当前节点的第一个子节点，以及最后一个子节点；包括空白文本

18、parentNode属性，表示当前节点的父节点

19、previousSibling属性，表示当前节点的前一个兄弟节点

20、nextSibling属性，表示当前节点的后一个兄弟节点

21、innerText可以获取文本内容，且没有标签；innerHTML有标签

22、document.body()

23、document.documentElement()

24、document.all()

25、document.getElementsByClassName()

26、document.querySelector()可以使用css选择器定位标签，总会返回一个元素

27、document.querySelectorAll()可以使用css选择器定位标签,返回数组

28、document.createElement()创建元素节点

29、document.createText()创建文本

30、appendChild()向父节点添加一个子节点

31、insertBefore()可以在指定的子节点前插入新的子节点，语法父节点.insertBefore(新节点，旧节点)

32、replaceChild()替换节点，语法父节点.replaceChild(新节点，旧节点)

33、removeChild()删除节点

34、confirm()确认和取消









