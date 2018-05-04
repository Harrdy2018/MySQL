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

***
# 主键约束
**作用：保证实体的完整性**
* Ex.1 为玩家表的QQ列添加主键约束,是玩家QQ这一列不能出现重复的值，也不能为空
```mysql
mysql> use test
Database changed
mysql> create table playerC(QQ varchar(20) not null primary key,playname varchar(50) not null,sex char(2) not null,
    ->  birthday date not null,mobile char(11) not null);
Query OK, 0 rows affected (0.26 sec)
```

# 外键约束
**保证引用的完整性**
* Ex.1 为分数表添加外键约束
```mysql
create table scores(
user_qq varchar(20) not null
references playerb(user_qq),
scores int not null
);
```

# 检查约束
**保证域完整性**
* Ex.1 为游戏表添加检查约束
```mysql
create table Games(
gno int not null check(gno>0),
gname varchar(50) not null,
gtype varchar(20) not null
);
```

# 默认约束
**保证域完整性**
* Ex.1 玩家表的性别默认为男性
```mysql
create table users(
user_qq VARCHAR(20) not null,
user_name VARCHAR(50) not null,
user_sex CHAR(2) not null DEFAULT'男',
user_birthday datetime not null,
ueser_phone char(11) not null
);
```

***
# 自增列
**保证实体完整性**
* Ex.1 游戏编号自增
```mysql
create table game(
gno int not null primary key auto_increment,
gname varchar(50) not null,
gtype varchar(20) not null
);
```

***
# 查看表基本结构
* describe/desc table_name
***
![查看表基本结构]()
***
