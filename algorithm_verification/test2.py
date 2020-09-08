from pyhive import hive

conn = hive.Connection(host='localhost', port=10002, username='hive', database='test')
cursor = conn.cursor()
sql = "select dst12 from traffic_matrices where srcid='12' limit 10;"
cursor.execute(sql)
str = " "
for result in cursor.fetchall():
	print(str.join(result))
