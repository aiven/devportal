import pymysql

timeout = 10
connection = pymysql.connect(

    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host=MYSQL_HOST,
    password=MYSQL_PASSWORD,
    read_timeout=timeout,
    port=MYSQL_PORT,
    user=MYSQL_USERNAME,
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE mytest (id INTEGER PRIMARY KEY)")
    cursor.execute("INSERT INTO mytest (id) VALUES (1), (2)")
    cursor.execute("SELECT * FROM mytest")
    print(cursor.fetchall())
finally:
    connection.close()
