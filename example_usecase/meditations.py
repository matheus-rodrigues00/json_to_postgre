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
with open('./meditations.json') as f:
    meditations = json.load(f)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Read the tag data from the JSON file
with open('./tags_output.json') as f:
    tag_data = json.load(f)

# Extract the tag name and ID pairs into a dictionary
tags = {tag['name'].lower(): tag['id'] for tag in tag_data}


# Loop through the JSON data and insert each record into the PostgreSQL table
for meditation in meditations:
    title = meditation['title']
    image_url = meditation['imageUrl']
    audio_file_url = meditation['audioVoice']
    audio_file_duration = meditation['time']
    published_at = meditation['createdAt']
    meditation_tags = meditation['tags']

    # Insert the record into the PostgreSQL table
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO meditations (title, image_url, audio_file_url, audio_file_duration, published_at)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (title, image_url, audio_file_url, audio_file_duration, published_at))
        meditation_id = cursor.fetchone()[0]

        # Insert the links between the meditation and its tags into the meditations_tags_links table
        for tag in meditation_tags:
            # get the corresponding tag_id from the tags dictionary
            tag_id = tags.get(tag.lower())
            if tag_id:
                cursor.execute("""
                    INSERT INTO meditations_tags_links (meditation_id, tag_id)
                    VALUES (%s, %s)
                """, (meditation_id, tag_id))

# Commit the changes and close the connection
conn.commit()
conn.close()
