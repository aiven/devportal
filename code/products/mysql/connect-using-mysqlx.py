import mysqlx

MYSQLX_PASSWORD = "user-password"
SERVICE_URI = "aiven-service-URI"
MYSQLX_USER = "mysqlx-user"

connection_data = f"mysqlx://{MYSQLX_USER}:{MYSQLX_PASSWORD}@{SERVICE_URI}/defaultdb?ssl-mode=REQUIRED"

session = mysqlx.get_session(connection_data)

# create a test schema
schema = session.create_schema("test")

# create a new collection in the schema
collection = schema.create_collection("food_prices")

# add entries to this collection
collection.add(
    {"type": "pizza", "price": "10e"},
    {"type": "burger", "price": "5e"},
).execute()


# read it back
for doc in collection.find().execute().fetch_all():
    print(f"Found document: {doc}")
