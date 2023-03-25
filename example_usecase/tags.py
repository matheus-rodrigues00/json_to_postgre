#!/usr/bin/env python
import psycopg2
import json

# PostgreSQL connection details
DB_HOST = "<database-host>"
DB_PORT = "<database-port>"
DB_NAME = "<database-name>"
DB_USER = "<database-username>"
DB_PASSWORD = "<database-password>"

# Read the JSON data from the file
with open('./tags.json') as f:
    tags = json.load(f)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Loop through the JSON data and insert each record into the PostgreSQL table
tag_id = 0
tags_obj = {}
for tag in tags:
    name = tag['tag']
    title = tag['title']
    subtitle = tag['subtitle']
    is_main = tag['major']
    # tag['createdAt']['seconds'] transforms the date into a timestamp
    created_at = tag['createdAt']
    # Insert the record into the PostgreSQL table
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO tags (name, title, subtitle, is_main, created_at)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (name, title, subtitle, is_main, created_at))

        tag_id = cursor.fetchone()[0]
        # Add the tag to the tags_obj dictionary
        tags_obj[name] = tag_id

with open('./tags_output.json', 'w') as f:
    json.dump(tags_obj, f)

# Commit the changes and close the connection
print(tags_obj)
conn.commit()
conn.close()
