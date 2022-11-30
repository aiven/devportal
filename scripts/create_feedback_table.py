import argparse
try:
    import psycopg2
except ImportError as e:
    print(e)
    print('To run this script, install psycopg2-binary. For instance:')
    print('    pip install psycopg2-binary')
    print('On some platforms, you may need to install PostgreSQL using your system')
    print('package manager to make that work')
    exit(1)

parser = argparse.ArgumentParser()
parser.add_argument('--pg-url', help='PostgreSQL URL')

if __name__ == '__main__':
    args = parser.parse_args()
    with psycopg2.connect(args.pg_url) as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE feedback (
                referrer text NOT NULL,
                vote text NOT NULL,
                message text NOT NULL,
                created_at timestamp NOT NULL
            );
            """)

    print("Feedback table created")
