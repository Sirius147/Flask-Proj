import pymysql
# connect 명령을 정상적으로 실행이되면, database인 madang과 접속한 상태가 됨
# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='root', password='root',
                       db='madang', charset='utf8')  

# Connection 으로부터 Cursor 생성
# curs : array based cursor (default)
curs = conn.cursor()

# SQL문 실행    # select all
sql = "select * from customer"
# excute는 dbms인 mysql과 직접 통신해서 sql 실행 결과값을 curs에 저장
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
print(rows)  # 전체 rows
# print(rows[0])  # 첫번째 row: (1, '박지성', '영국 맨체스타', '000-5000-0001')
# print(rows[1])  # 두번째 row: (2, '김연아', '대한민국 서울', '000-6000-0001')

# Connection 닫기
conn.close()