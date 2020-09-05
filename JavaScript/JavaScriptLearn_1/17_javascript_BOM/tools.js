//用来获取指定元素的当前样式
function move(obj, attr, target, speed, callback){
	clearInterval(obj.timer);
	var current = parseInt(getStyle(obj, "left"));
	if(current>target){
		speed = -speed;
	}
	//开启一个定时器,用来执行动画效果
	//向执行动画的对象中添加一个timer属性,用来保存它自己的定时器的标识
	obj.timer = setInterval(function(){
		var oldValue = parseInt(getStyle(obj, attr));
		//在旧值的基础上增加
		var newValue = oldValue + speed;
		if((speed < 0 && newValue < target) || (speed > 0 && newValue > target)){
			newValue = target;
		}
		//将新值设置给box1
		obj.style[attr] = newValue + "px";
		if(newValue == target){
			clearInterval(obj.timer);
			//动画执行完毕调用回调函数
			callback && callback();
		}
	},30);
}
function getStyle(obj,name){
	if(window.getComputedStyle){
		//正常浏览器
		return getComputedStyle(obj, null)[name];
	}else{
		//IE8的方式
		return obj.currentStyle[name];
	}
}