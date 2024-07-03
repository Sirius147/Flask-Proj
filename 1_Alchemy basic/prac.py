import pymysql

# connection with mysql
# make cursor
# execute sql inst
# fetch db

con=pymysql.connect(host="localhost",user='root',password='root',
                    db='madang', charset='utf8')
curs=con.cursor()

sql= 'select * from books' # 'select * from books where price >= %s and publisher like %s'

curs.execute(sql) # curs.execute(sql, (10000, '동아'))


'''
sql = 'insert into books (bookid,publisher,prcice) values(%s,%s,%s)''
curs.execute(sql, (223,'동아', 10000))

curs.commit()

sql = 'update books set publisher='한솔' where publisher='동아''
curs.excute(sql)
curs.commit()

sql = 'delete from books where price < 10000 OR price > 100000'"
curs.execute(sql)
curs.commit()
'''

#restaurant_sql = 
'''create table restaurant ( menu_name = char(18) not null,
 recipe = varchar,
 num_staff = number(10,0)
  primary key( menu_name)
   foreign key( restaurant_id) references customer(local_id) check(local_id > 0) )'''
tuples=curs.fetchall()

print(tuples)


# free connection

curs.close()
