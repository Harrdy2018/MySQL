# MySQL
* [如何创建一张表](#如何创建一张表)
* [主键约束](#主键约束)
* [外键约束](#外键约束)
* [检查约束](#检查约束)
* [默认约束](#默认约束)
* [自增列](#自增列)
* [查看表基本结构](#查看表基本结构)
* [查看表详细结构](#查看表详细结构)
* [修改表名](#修改表名)
* [修改字段名](#修改字段名)
* [修改字段数据类型](#修改字段数据类型)
* [添加删除字段](#添加删除字段)
* [增补约束](#增补约束)
* [删除无关联数据表](#删除无关联数据表)
* [删除有关联数据表](#删除有关联数据表)
* [插入数据](#插入数据)
* [修改数据](#修改数据)
* [](#)

***
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
![查看表基本结构](https://github.com/Harrdy2018/MySQL/blob/master/MySQL1.png)
***
```
Field:字段名
Type:字段类型
NULL:是否可以为空
Key:是否编制索引
Default:默认值
Extra:附加信息，如自增列
```

***
# 查看表详细结构
* show create table table_name
```MySQL
mysql> use test
Database changed
mysql> show create table game \G
*************************** 1. row ***************************
       Table: game
Create Table: CREATE TABLE `game` (
  `gno` int(11) NOT NULL AUTO_INCREMENT,
  `gname` varchar(50) NOT NULL,
  `gtype` varchar(20) NOT NULL,
  PRIMARY KEY (`gno`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8
1 row in set (0.00 sec)
```
**如果不加\G信息会非常乱，相当于格式化输出；展示整张表的创建过程！！！**

***
# 修改表名
* alter table old_name rename to new_name
```MySQL
mysql> use test
Database changed
mysql> alter table game rename to QQ_game;
Query OK, 0 rows affected (0.20 sec)
```

***
# 修改字段名
* alter table table_name
* change old_name new_name new_type
```MySQL
mysql> use test
Database changed
mysql> alter table game
    -> change gno game_id varchar(20);
Query OK, 2 rows affected (0.75 sec)
Records: 2  Duplicates: 0  Warnings: 0
```

***
# 修改字段数据类型
* alter table table_name
* modify col_name new_type
```MySQL
mysql> use test
Database changed
mysql> alter table game
    -> modify gno varchar(20);
Query OK, 2 rows affected (0.55 sec)
Records: 2  Duplicates: 0  Warnings: 0
```

***
# 添加删除字段
* alter table table_name
* add new_col_name new_type
***
* alter table table_name
* drop col_name
```MySQL
mysql> use test
Database changed
mysql> alter table game
    -> add a int;
Query OK, 0 rows affected (0.60 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table game
    -> drop a;
Query OK, 0 rows affected (0.45 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

***
# 增补约束
* 添加主键语法
* alter table table_name
* add constraint con_name
* primary key(col_name)
```MySQL
mysql> use test
Database changed
mysql> alter table users
    -> add constraint pk_users_userqq
    -> primary key(userqq);
Query OK, 0 rows affected (0.40 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

***
* 添加外键约束
* alter table f_table
* add constraint con_name
* foreign key(f_col) references m_table(m_col)

***
* 添加检查约束
* alter table table_name
* add constraint con_name
* check(exp)

***
* 添加默认值
* alter table table_name
* alter col_name set default value

***
* 添加自动增长
* alter table table_name
* modify column col_name col_type col_null auto_increment
* primary key

***
# 删除无关联数据表
* drop table [if exists] table_name1,table_name2

***
# 删除有关联数据表
* alter table f_table_name drop foreign key con_name
* drop table table1,table2...

***
# 插入数据
* 所有列都插入值 insert [into] table_name values(v1,v2...vn);
* 如果插入的值有默认值的话，可以用关键值default代替
* 为特定列插入值 insert [into] table_name(col1,col2...coln) values(v1,v2...vn);
* 一次性插入多条记录 insert [into] table_name(col1,col2...coln) values(v1,v2...vn),(v1,v2...vn)...;

***
# 修改数据
* 修改全部数据 update table_name set{col_name=expression}[...n];
* 列上的值全部加上100 update scores set score=score+100;
* 修改特定数据 update table_name set{col_name=expression}[...n] where condition_expression;

***
# 删除数据
* 使用delete命令删除数据 delete [from] table_name [where condition_expression];
* 使用truncate table删除数据 truncate table table_name;清空表中的数据

***
# 查询
* 查询和提取数据的过程是客户端和服务器交互的过程
```
select col1,col2...coln
from table1,table2...tablen
[where conditions]
[group by group_by_list]
[having conditions]
[order by order_list [asc|desc]]
```
* 查询表的全部行和列 select user_qq,user_name,user_sex,user_birthday,user_phone from users;
* 查询表的全部行和列 select `*` from users;
* 查询表的部分列 select user_qq,user_name from users;
* 别名使用 select user_qq as '玩家QQ',user_name as '玩家姓名' from users;
* 别名使用 select user_qq '玩家QQ',user_name '玩家姓名' from users;
* distinct关键字 消除结果集中的重复行 select distinct user_qq from scores;
* limit关键字 指定结果集中数据的显示范围 select `*` from users limit 2,3;
* limit关键字 只显示3条数据 select `*` from users limit 3;
