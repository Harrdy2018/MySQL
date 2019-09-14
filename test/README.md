## 题目
### 创建表
* Student
```sql
MariaDB [test2018]> show create table Student \G;
*************************** 1. row ***************************
       Table: Student
Create Table: CREATE TABLE `Student` (
  `s_id` varchar(20) NOT NULL,
  `s_name` varchar(20) NOT NULL DEFAULT '',
  `s_birth` varchar(20) NOT NULL,
  `s_sex` varchar(20) NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)

ERROR: No query specified

MariaDB [test2018]> select * from Student;
+------+----------+------------+-------+
| s_id | s_name   | s_birth    | s_sex |
+------+----------+------------+-------+
| 01   | zhaolei  | 1990-01-01 | nan   |
| 02   | qiandian | 1990-12-21 | nan   |
| 03   | sunfeng  | 1990-05-20 | nan   |
| 04   | liyun    | 1990-08-06 | nan   |
| 05   | zhoumei  | 1991-12-01 | nv    |
| 06   | wunan    | 1992-03-01 | nv    |
| 07   | zhenzhu  | 1989-07-01 | nv    |
| 08   | wangju   | 1990-01-20 | nv    |
+------+----------+------------+-------+
8 rows in set (0.00 sec)
```
* Teacher
```sql
MariaDB [test2018]> show create table Teacher \G;
*************************** 1. row ***************************
       Table: Teacher
Create Table: CREATE TABLE `Teacher` (
  `t_id` varchar(20) NOT NULL,
  `t_name` varchar(20) NOT NULL,
  PRIMARY KEY (`t_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)

ERROR: No query specified

MariaDB [test2018]> select * from Teacher;
+------+----------+
| t_id | t_name   |
+------+----------+
| 01   | zhangsan |
| 02   | lishi    |
| 03   | wangwu   |
+------+----------+
3 rows in set (0.01 sec)
```
* Score
```sql
MariaDB [test2018]> show create table Score \G;
*************************** 1. row ***************************
       Table: Score
Create Table: CREATE TABLE `Score` (
  `s_id` varchar(20) NOT NULL,
  `c_id` varchar(20) NOT NULL,
  `s_score` int(3) DEFAULT NULL,
  PRIMARY KEY (`s_id`,`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)

ERROR: No query specified

MariaDB [test2018]> select * from Score;
+------+------+---------+
| s_id | c_id | s_score |
+------+------+---------+
| 01   | 01   |      80 |
| 01   | 02   |      90 |
| 01   | 03   |      99 |
| 02   | 01   |      70 |
| 02   | 02   |      60 |
| 02   | 03   |      80 |
| 03   | 01   |      80 |
| 03   | 02   |      80 |
| 03   | 03   |      80 |
| 04   | 01   |      50 |
| 04   | 02   |      30 |
| 04   | 03   |      20 |
| 05   | 01   |      76 |
| 05   | 02   |      87 |
| 06   | 01   |      31 |
| 06   | 03   |      34 |
| 07   | 02   |      89 |
| 07   | 03   |      98 |
+------+------+---------+
18 rows in set (0.00 sec)
```
* Course
```sql
MariaDB [test2018]> show create table Course \G;
*************************** 1. row ***************************
       Table: Course
Create Table: CREATE TABLE `Course` (
  `c_id` varchar(20) NOT NULL,
  `c_name` varchar(20) NOT NULL,
  `t_id` varchar(20) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)

ERROR: No query specified

MariaDB [test2018]> select * from Course;
+------+--------+------+
| c_id | c_name | t_id |
+------+--------+------+
| 01   | yuwen  | 02   |
| 02   | shuxue | 01   |
| 03   | yingyu | 03   |
+------+--------+------+
3 rows in set (0.00 sec)
```
### solve
* [1、查询"01"课程比"02"课程成绩高的学生的信息及课程分数](./1.md)
