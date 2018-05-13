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
* [删除数据](#删除数据)
* [查询](#查询)
* [汇总和分组数据](#汇总和分组数据)
* [连接查询](#连接查询)
* [子查询](#子查询)

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
* 普通条件查询 select * from users where user_qq='1035525823';
* 普通条件查询 select * from scores where scores>200;
```
比较运算符
等于                                 =
不等于                               <>
大于                                 >
大于等于                             >=
小于                                 <
小于等于                             <=
```
* 普通条件查询 select * from scores where gno=1 and scores>200;
```
逻辑运算符
并且                                 and
或者                                 or
非                                   not
```
* 模糊查询 select * from scores where scores>2500 and score<=3000;
* 模糊查询 select * from scores where score between 2500 and 3000;此方法边界全部包含，这两个数字不能换位置，也就是2500<=x<=3000
* 模糊查询 select * from scores where score not between 2500 and 3000;
```
通配符
_     一个字符
%     任意长度 
[]    指定范围内
[^]   不在括号中
```
* select `*` from users where user_name like '孙%';
* select `*` from users where user_name not like '孙%';
```
查询空值的运算符
select * from users where user_birthday is null;
select * from users where user_birthday is not null;
```

***
```
select col_list from table_name order by order_by_list[asc|desc]

select * from scores where gno=1 
order by score asc;

select * from scores where gno=1 
order by score desc;

多列排序
select * from scores
order by gno asc,score desc;
```

***
# 汇总和分组数据
* 聚合函数：对多条记录作统计
***
|聚合函数|数据类型|描述|
|:-----|:-----|:-----|
|sum()|数字|对指定列的所有非空值求总和|
|avg()|数字|对指定列的所有非空值求平均值|
|min()|数字，字符，datetime|返回指定列中的最小数字，最早的日期或者最小的字符串|
|max()|数字，字符，datetime|返回指定列中的最大数字，最近的日期或者最大的字符串|
|count()|任意基于行的数据类型|统计结果集合中全部记录行的数量|
***
* select count(user_qq) from users;
* select count(`*`) from users;
* select sum(score) as '总分数' from scores where user_qq='12301';
* select avg(score) as '平均分数' from scores where user_qq='12302';
* select max(score) as '最高分数' from scores where gno=1;
```
select
sum(score) as '总分数',
avg(score) as '平均分数',
max(score) as '最高分数'
from scores where user_qq='12301';
```

***
* 在结果集内分组
* 使用group by分组
```
select user_qq,
sum(score) as '总分数',
avg(score) as '平均分数',
max(score) as '最高分数'
from scores
group by user_qq

select user_qq,
avg(score) as '平均分数'
from scores
group by user_qq
```

***
* 筛分组结果
```
select user_qq,
sum(score) as '总分数',
avg(score) as '平均分数',
from scores
group by user_qq
having avg(score)>4000

select user_qq,
sum(score) as '总分数',
avg(score) as '平均分数',
from scores
group by user_qq
order by avg(score) desc
```

***
* select语句执行顺序
* from指定数据源
* where第一次筛选
*　group by分组
* 使用聚合函数统计
* having字句筛选分组
* 使用order by排序

***
# 连接查询
```
如果昵称在users表，游戏名在games表，分数在scores表
select user_name as '昵称',
game as '游戏名称',
score as '分数'
from users,games,scores
where users.user_qq=scores.user_qq and games.gno=scores.gno

内连接
相连接的两张表地位平等
如果一张表中在另一张表不存在对应数据，则不做连接
select user_name as '昵称',
score as '分数'
from users,scores
where users.user_qq=scores.user_qq and games
from字句后面出现多个表名，这种连接方式即属于内连接，是隐式内连接

显示内连接格式
select col_list
from table1 [inner] join table2
on table1.col=table2.col

select user_name as '昵称',
game as '游戏名称',
score as '分数'
from games inner join scores
on games.gno=scores.gno
inner join users
on users.user_qq=scores.user_qq

查询每个玩家的昵称，总分和平均分
select user_name as '昵称',
sum(score) as '总分',
avg(score) as '平均分'
from users u inner join scores s
on s.user_qq=u.user_qq
group by u.user_qq,u.user_name

查询平均分大于3500的分数信息，显示玩家昵称，总分，平均分，并按照平均分数将降序排列
select user_name as '昵称',sum(score) as '总分',avg(score) as '平均分'
from users u inner join scores s
on s.user_qq=u.user_qq
group by u.user_qq,u.user_name
having avg(score)>3500
order by avg(score) desc

外连接
左外连接和右外连接
做连接的两个表地位不平等，其中一张是基础表
基础表中的每条数据是必出现的，即使没有，用null补
左外连接左是基础表，右外连接右是基础表
语句中先出现的表为左表，后出现的表为右表
select col_list
from table1 left|right[outer] join table2
on table1.col=table2.col

要求查询所有关于5号游戏的分数信息
select user_name as '昵称',gno as '游戏编号',score as '分数'
from users u left join scores s
on u.user_qq=s.user_qq
and s.gno=5
```

***
# 子查询
```
使用in关键字的子查询
    查询游戏类型是“棋牌类”的游戏的分数信息
游戏分数表中并未包含游戏类型信息
思路一：采用连接查询
思路二：分两步进行，首先找到所有“棋牌类”游戏的编号，再以这一组编号为查询依据完成查询
select * from scores where gno in
(select gno from games where gtype="棋牌")

查询没有参与5号游戏的玩家QQ
select user_qq from users
where user_qq not in
(select user_qq from scores where gno=5)

使用exists关键字的子查询
    如果存在昵称为“孙悟空”，则查询分数表中数据
select * from scores
where exists
(select * from users where user_name='孙悟空')
```

***
# 联合查询
* 可以把多条查询语句所产生的结果集纵向连接为一体
* 有all关键字可以显示全部数据（即重复的也显示出来）
* 列的数量与类型要兼容

```
select user_name from users
union
select gname from games

查询玩家表中所以女性玩家和生日为空的玩家
select * from users where user_sex='女'
union
select * from users where user_birthday is null

select * from users where user_sex='女' or user_birthday is null

查询QQ号是"12301"的玩家所有分数并计算出总分和平均分，并显示到同一个结果集中
select user_qq,gno,score from scores
where user_qq='12301'
union all
select '总分',' ',sum(score) from scores where user_qq='12301'
union all
select '平均分',' ',AVG(score) from scores where user_qq='12301'
```
