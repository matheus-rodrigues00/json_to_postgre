#!/usr/bin/env python
import psycopg2
import json

# PostgreSQL connection details
DB_HOST = "<database-host>"
DB_PORT = "<database-port>"
DB_NAME = "<database-name>"
DB_USER = "<database-username>"
DB_PASSWORD = "<database-password>"
TABLE_NAME = "<table-name>"

# Read the JSON data from the file
with open('./data.json') as f:
    data = json.load(f)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Loop through the JSON data and insert each record into the PostgreSQL table
for item in data:
    # Replace the keys below with the keys in your JSON data
    name = item['name']
    title = item['title']
    subtitle = item['subtitle']
    created_at = item['created_at']

    # Insert the record into the PostgreSQL table
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO {} (name, title, subtitle, created_at)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """.format(TABLE_NAME), (name, title, subtitle, created_at))

conn.commit()
conn.close()
