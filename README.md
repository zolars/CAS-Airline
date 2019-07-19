# Echarts 航线绘图

需求1: 页面底部为使用 echarts 绘制全球2D地图, 页面右侧增加用户列表窗口

需求2: 点击右侧的某个人物, 在全球2D地图上绘制该人物相关的所有飞机航线(动态效果), 并且在页面左侧显示人物详细信息窗口; 再次点击该人物时, 隐藏该人物相关航线, 隐藏人物相信信息窗口

![img](https://raw.githubusercontent.com/zolars/typora-user-images/master/clip_image002.jpg)

![img](https://raw.githubusercontent.com/zolars/typora-user-images/master/clip_image004.jpg)

航线动态效果参考: <https://gallery.echartsjs.com/editor.html?c=xfkyn0TV0G>

数据格式: json

JSON.json文件: 存放人物及航线数据, 如下图所示, airlines为人物"Amy"的所有航线记录, 共三条, 每条包括起点坐标和终点坐标。

![img](https://raw.githubusercontent.com/zolars/typora-user-images/master/clip_image006.gif)