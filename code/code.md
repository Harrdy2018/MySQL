## 自动化数据库测试
### 背景
```
我们知道有关数据库的测试中，如果手工的进行一系列表单的建立，修改，是相当费时的，更不用说还要测试数据库运行过程中的监控状态是否正常，
所以在测试中很有必要编写一下脚本来进行自动化测试的
```
```
数据库方面的测试主要包括两个方面，
第一个方面：数据库功能是否正常，也就是增，删，改，查。
第二个方面：动态监控数据库运行状态，包括，容量大小，参数动态变化等，
所以单纯用手工来测试，实现第二个方面的测试就非常困难。
所以有必要采用自动化测试的技术，权衡时间目的的投入产出比，最终决定采用shell 脚本来实现自动化测试。
```
* 初始化数据库
```shell
#! /bin/bash
echo "Run create tempTable"
mysql --host=0.0.0.0 --port=3306 --user=root --password=1234 -e \
"drop database if exists tempDB; \
create database tempDB; \
use tempDB; \
create table if not exists tempTable(id int(4),name varchar(10),info varchar(30),mobile int(20),primary key(id)); \
show create table tempTable \G; \
\q;"
echo "have done"
```
* 手工建表
```shell
#! /bin/bash
echo "Run create data"
for i in {1..3}
do
mysql --host=0.0.0.0 --port=3306 --user=root --password=1234 -e \
"use tempDB; \
insert into tempTable values($i,'Tom','gasghahda',1223231); \
select * from tempTable where id=$i; \
replace into tempTable(id,name,info,mobile) values($i,'lukang','I love you haha!!',18260031951); \
select * from tempTable where name='lukang'; \
update tempTable set name='Harrdy' where id=$i; \
select * from tempTable where id=10; \
select sleep(3); \
\q;"
echo "have done"
done
```