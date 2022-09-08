from pymysql import *
import pymysql.cursors
import time

print('Connecting to EC2 MySQL database...')
conn = connect(host='localhost', user='root', password='wustl-inst', db='performance_test', cursorclass=pymysql.cursors.DictCursor)
print('Connected to EC2 MySQL database')
with conn:
  with conn.cursor() as cursor:
    sql = 'CREATE TABLE IF NOT EXISTS `ec2_test` (`id` int(11) NOT NULL AUTO_INCREMENT, `name` varchar(255) NOT NULL, `age` int(11) NOT NULL, PRIMARY KEY (`id`));'
    cursor.execute(sql)
    sql = 'INSERT INTO `ec2_test` (`name`, `age`) VALUES (%s, %s);'
    cursor.execute(sql, ('Quan Khuc', 23))
    sql = 'INSERT INTO `ec2_test` (`name`, `age`) VALUES (%s, %s);'
    cursor.execute(sql, ('Khoa Vu', 24))
    sql = 'INSERT INTO `ec2_test` (`name`, `age`) VALUES (%s, %s);'
    cursor.execute(sql, ('Mia Khalifa', 29))
    sql = 'INSERT INTO `ec2_test` (`name`, `age`) VALUES (%s, %s);'
    cursor.execute(sql, ('Peter Reuling', 24))
    sql = 'INSERT INTO `ec2_test` (`name`, `age`) VALUES (%s, %s);'
    cursor.execute(sql, ('Robert Krauss', 24))
  conn.commit()