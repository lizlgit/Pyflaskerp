# 基础级别的flask构架制作的库存登记查询DEMO
## 使用Python3.6+Flask+MySQL
## 针对受众是刚刚入门的Python学习者，很基础的内容,条理比较清晰
## 半成品都还没达到，所以可能某些页面还没做的点击进去会报错，后退即可
## 运行环境
1. 安装第三方包：
>pip3 install flask_sqlalchemy==2.1
>pip3 install Flask
>pip3 install flask_login
2. 数据库使用MYSQL，我转了一个SQL文件，可直接运行，也可通过类生成
>/SQL/ERPdemo.sql
3. 启动需要修改的地方
>数据库连接在setting.py文件内，内容类似这样username:pwd@addr:port/dbname
>启动即可
## 程序结构
#### main.py--主程序，存放路由及主要内容
#### models.py--数据库ORM模型的类定义
#### setting.py--数据库链接使用的配置
#### shapasswd.py--加密，使用hash进行多次加密的典型做法
#### sqlmath.py--数据操作程序，把要做的内容定义一下，做成函数给主程序使用
## 前端说明
#### 使用layui做的简易前端，感觉并不理想，功能有限，可能重做
#### 登陆页面别人那里拿来的
## 接下来准备做的
#### 页面补全，至少不会跳死
#### 功能补全
#### 登陆系统，明显现在是不能控制登陆的，所以才说demo
