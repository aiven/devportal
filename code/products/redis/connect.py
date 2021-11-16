import redis


def main():
    redis_uri = 'REDIS_URI'
    redis_client = redis.from_url(redis_uri)

    redis_client.set('key', 'hello world')
    key = redis_client.get('key').decode('utf-8')

    print('The value of key is:', key)


if __name__ == '__main__':
    main()
