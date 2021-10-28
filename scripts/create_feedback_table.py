import argparse
import psycopg2

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