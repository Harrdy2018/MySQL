# MySQL

# 如何创建一张表
* 命令行窗口创建表
```mysql
mysql> use test
Database changed
mysql> create table t2(
    -> r1 int not null,
    -> r2 varchar(5) not null);
Query OK, 0 rows affected (0.32 sec)
```
```
我的数据库密码是1234,test是一个数据库，use test表示切换到当前数据库
怎么样调命令行窗口的背景？将鼠标移到命令行顶部的空白区域，右键属性
```

* Navicat创建数据表
* 直接找到test库的tables新建一张表就可以了
* 或者点击Query-->>New Query，然后在里面输入创表语句，怎么样样把字体调大？按住ctrl向上滚动鼠标轮
