import psycopg2


def main():
    conn = psycopg2.connect('POSTGRESQL_URI')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    main()
