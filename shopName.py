import MySQLdb
import sys

#쇼핑몰 이름 가져오기
shopName = sys.argv[1]


#관리자 데이터 등록(상의 이미지 분석)
#DB연동
con = MySQLdb.connect(host="127.0.0.1", port=3309, user="man01", passwd="man01", db="user")
Cursor = con.cursor()

con.set_character_set('utf8')
Cursor.execute('SET NAMES utf8;')
Cursor.execute('SET CHARACTER SET utf8;')
Cursor.execute('SET character_set_connection=utf8;')
  
#DB에 상의 정보와 이미지파일 등록
sql = "SELECT MAX(num) FROM style"
Cursor.execute(sql)

row = Cursor.fetchone()
num = row[0]

sql = "UPDATE style SET shopname=%s WHERE num=%s"
val = (shopName, num)
Cursor.execute(
	sql, val
)
con.commit()	
con.close()