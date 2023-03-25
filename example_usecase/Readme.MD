# Example use case
## Usage
1. First, you need to create a PostgreSQL database and table that you want to migrate your JSON data into.
2. Next, create a JSON file with your data that you want to migrate. For example, meditations.json:
```
[
{
    "title": "Meditation for Relaxation",
    "description": "This guided meditation will help you relax and release tension in your body and mind.",
    "image_url": "https://example.com/images/meditation.jpg",
    "is_free": true,
    "audio_file_duration": 1800,
    "allow_background_music": true,
    "published_at": "2022-03-25T09:00:00Z",
    "audio_file_url": "https://example.com/meditations/relaxation.mp3",
    "tags": [
        "Relaxation",
        "Stress Relief",
        "Guided Meditation"
    ]
},
{
    "title": "Meditation for Sleep",
    "description": "This guided meditation will help you relax and fall asleep.",
    "image_url": "https://example.com/images/meditation.jpg",
    "is_free": true,
    "audio_file_duration": 1800,
    "allow_background_music": true,
    "published_at": "2022-03-25T09:00:00Z",
    "audio_file_url": "https://example.com/meditations/sleep.mp3",
    "tags": [
        "Sleep",
        "Guided Meditation"
    ]
}
]

```
3. Create a JSON file with the data that you want to use as tags or any other relational table. For example, tags.json:
```
[
    {
        "name": "Tag1",
        "title": "Tag 1",
        "subtitle": "Subtitle for Tag 1",
        "is_main": true,
        "created_at": "2022-03-01T12:00:00.000Z"
    },
    {
        "name": "Tag2",
        "title": "Tag 2",
        "subtitle": "Subtitle for Tag 2",
        "is_main": true,
        "created_at": "2022-03-01T12:00:00.000Z"
    },
    {
        "name": "Tag3",
        "title": "Tag 3",
        "subtitle": "Subtitle for Tag 3",
        "is_main": false,
        "created_at": "2022-03-01T12:00:00.000Z"
    }
]
```
4. Edit the json_to_postgresql.py script to match your database and table information:
```
# PostgreSQL connection details
DB_HOST = "<database-host>"
DB_PORT = "<database-port>"
DB_NAME = "<database-name>"
DB_USER = "<database-username>"
DB_PASSWORD = "<database-password>"
TABLE_NAME = "<table-name>"
```
5. Run the tags.py script (order important) to insert the tags into the PostgreSQL database (o).
6. Run the meditations.py script to migrate the JSON data into the PostgreSQL database while making relations.