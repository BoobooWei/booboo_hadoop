# Hive SQL

```shell
[hadoop@mastera0 ~]$ cat emp.txt
1	booboo	DBA	hello	2013-12-26	3000.00	30	1
2	batman	DBA	baby	2011-1-12	5000.00	50	1
[hadoop@mastera0 ~]$ cat dept.txt
1	dba	klsjdflkdsjflk

\#---------------------------

hive> show databases;
OK
default
Time taken: 0.491 seconds, Fetched: 1 row(s)
hive> create database db_hive_01;
OK
Time taken: 0.362 seconds
hive> show databases;
OK
db_hive_01
default
Time taken: 0.018 seconds, Fetched: 2 row(s)
hive> use db_hive_01;
OK
Time taken: 0.019 seconds
hive> desc database db_hive_01;
OK
db_hive_01		hdfs://172.25.0.11:8020/user/hive/warehouse/db_hive_01.db	hadoop	USER	
Time taken: 0.026 seconds, Fetched: 1 row(s)
hive> drop database db_hive_01 cascade;
OK
Time taken: 0.129 seconds
hive> create database db_hive_01;      
OK
Time taken: 0.056 seconds
hive> drop database db_hive_01;
OK
Time taken: 0.033 seconds
hive> create database db_hive_01;
OK
Time taken: 0.046 seconds
hive> use db_hive_01;
OK
Time taken: 0.01 seconds
hive> create table emp (    
    > empno int,
    > ename string,
    > job string,
    > mgr int,
    > hiredate string,
    > sal double,
    > comm double,
    > deptno int
    > )
    > row format delimited fields terminated by '\t';
OK
Time taken: 0.153 seconds
hive> create table dept (
    > deptno int,
    > dname string,
    > loc string)
    > row format delimited fields terminated by '\t';
OK
Time taken: 0.083 seconds
hive> load data local inpath 'emp.txt' into table emp;
Loading data to table db_hive_01.emp
Table db_hive_01.emp stats: [numFiles=1, numRows=0, totalSize=84, rawDataSize=0]
OK
Time taken: 0.466 seconds
hive> load data local inpath 'dept.txt' into table dept;
Loading data to table db_hive_01.dept
Table db_hive_01.dept stats: [numFiles=1, numRows=0, totalSize=21, rawDataSize=0]
OK
Time taken: 0.282 seconds
hive> select * from emp;
OK
1	booboo	DBA	NULL	2013-12-26	3000.0	30.0	1
2	batman	DBA	NULL	2011-1-12	5000.0	50.0	1
Time taken: 0.079 seconds, Fetched: 2 row(s)
hive> select * from dept;
OK
1	dba	klsjdflkdsjflk
Time taken: 0.068 seconds, Fetched: 1 row(s)

```




