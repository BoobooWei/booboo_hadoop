# Hive Install

## 解压Hive并修改配置文件

```shell
[root@mastera0 ~]# cd /usr/local/hive-0.13.1-cdh5.3.6/
[root@mastera0 hive-0.13.1-cdh5.3.6]# 
<property>
  <name>hive.metastore.warehouse.dir</name>
  <value>/user/hive/warehouse</value>
  <description>location of default database for the warehouse</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionURL</name>
  <value>jdbc:mysql://172.25.0.11:3306/hive?useSSL=no</value>
  <description>JDBC connect string for a JDBC metastore</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionDriverName</name>
  <value>com.mysql.jdbc.Driver</value>
  <description>Driver class name for a JDBC metastore</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionUserName</name>
  <value>bigdata</value>
  <description>username to use against metastore database</description>
</property>

<property>
  <name>javax.jdo.option.ConnectionPassword</name>
  <value>(Uploo00king)</value>
  <description>password to use against metastore database</description>
</property>

```

## 安装 mysql 5.7 并授权

```shell
> grant all on *.* to  bigdata@'172.25.0.11' identified by '(Uploo00king)'
> create database hive;
```

## 添加API

```shell
[root@mastera0 lib]# pwd
/usr/local/hive-0.13.1-cdh5.3.6/lib
[root@mastera0 lib]# chmod 755 mysql-connector-java-5.1.41-bin.jar 

-rwxr-xr-x   1 root root   992808 Apr  7 11:12 mysql-connector-java-5.1.41-bin.jar
```

## Hive仓库目录

* hive临时目录 `hadoop fs -mkdir /tmp`
* hive仓库目录 `hadoop fs -mkdir -p /user/hive/warehouse`
* 修改临时目录权限 `hadoop fs -chmod g+w /tmp`
* 修改仓库目录权限 `hadoop fs -chmod g+w /user/hive/warehouse`

ps: `hadoop fs` = `hdfs dfs`

## Hive日志

```shell
[root@mastera0 ~]# cd /usr/local/hive-0.13.1-cdh5.3.6/conf
[root@mastera0 conf]# cp hive-log4j.properties.template hive-log4j.properties
[root@mastera0 hive-0.13.1-cdh5.3.6]# mkdir logs
[root@mastera0 hive-0.13.1-cdh5.3.6]# vim conf/hive-log4j.properties
hive.log.dir=/usr/local/hive-0.13.1-cdh5.3.6/logs
```

## 启动hive

```shell

[root@mastera0 conf]# chown hadoop. /usr/local/hive-0.13.1-cdh5.3.6/ -R
[root@mastera0 conf]# su - hadoop
Last login: Fri Apr  7 10:57:07 CST 2017 from 172.25.0.250 on pts/0
[hadoop@mastera0 ~]$ cat test2.txt
1
2
3
4
[hadoop@mastera0 ~]$ hive
17/04/07 13:15:00 WARN conf.HiveConf: DEPRECATED: hive.metastore.ds.retry.* no longer has any effect.  Use hive.hmshandler.retry.* instead

Logging initialized using configuration in file:/usr/local/hive-0.13.1-cdh5.3.6/conf/hive-log4j.properties
hive> show tables;
OK
Time taken: 0.493 seconds
hive> create table booboo (id tinyint,name varchar(20));
OK
Time taken: 0.576 seconds
hive> show tables;
OK
booboo
Time taken: 0.023 seconds, Fetched: 1 row(s)
hive> create table test2 (id int) row format delimited fields terminated by '\t';
OK
Time taken: 0.073 seconds
hive> load data local inpath 'test2.txt' into table test2;
Loading data to table default.test2
Table default.test2 stats: [numFiles=1, numRows=0, totalSize=8, rawDataSize=0]
OK
Time taken: 0.216 seconds
hive> select * from test2;
OK
1
2
3
4
Time taken: 0.065 seconds, Fetched: 4 row(s)
hive> select id from test2;
Total jobs = 1
Launching Job 1 out of 1
Number of reduce tasks is set to 0 since there's no reduce operator
Starting Job = job_1491538637923_0001, Tracking URL = http://mastera0.example.com:8088/proxy/application_1491538637923_0001/
Kill Command = /hadoop/hadoop-2.5.0-cdh5.3.6/bin/hadoop job  -kill job_1491538637923_0001
Hadoop job information for Stage-1: number of mappers: 1; number of reducers: 0
2017-04-07 14:06:51,861 Stage-1 map = 0%,  reduce = 0%
2017-04-07 14:06:58,219 Stage-1 map = 100%,  reduce = 0%, Cumulative CPU 1.04 sec
MapReduce Total cumulative CPU time: 1 seconds 40 msec
Ended Job = job_1491538637923_0001
MapReduce Jobs Launched: 
Stage-Stage-1: Map: 1   Cumulative CPU: 1.04 sec   HDFS Read: 221 HDFS Write: 8 SUCCESS
Total MapReduce CPU Time Spent: 1 seconds 40 msec
OK
1
2
3
4
Time taken: 16.543 seconds, Fetched: 4 row(s)

hive> create table stu2 (id int);
OK
Time taken: 0.072 seconds
hive> load data local inpath 'stu.txt' into table stu2;
Loading data to table default.stu2
Table default.stu2 stats: [numFiles=1, numRows=0, totalSize=8, rawDataSize=0]
OK
Time taken: 0.184 seconds
hive> select * from stu2;
OK
1
2
3
4
Time taken: 0.055 seconds, Fetched: 4 row(s)
hive> drop table stu2;
OK
Time taken: 0.123 seconds
hive> dfs -ls /;
Found 3 items
drwxr-xr-x   - hadoop supergroup          0 2017-04-05 15:22 /booboo
drwxrwx---   - hadoop supergroup          0 2017-04-07 13:17 /tmp
drwxr-xr-x   - hadoop supergroup          0 2017-04-07 12:20 /user

hive> dfs -cat /user/hive/warehouse/test2/test2.txt;
1
2
3
4
hive> exit;


