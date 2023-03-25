# JSON to PostgreSQL Migration Script
This is a generic Python script that can be used to migrate data from a JSON file to a PostgreSQL database. It is also designed to work with any JSON file and any PostgreSQL table, making it a flexible solution for various migration tasks.

## Dependencies
This script requires the psycopg2 library to be installed. You can install it using pip:

```
pip install psycopg2
```

## Usage
1. Run the generate_mock.py script to generate sample data in data.json.
```
python generate_mock.py
```
2. Review the generated data in data.json to ensure that it meets your requirements.
3. Update the PostgreSQL connection details in json_to_postgre.py. Replace <database-host>, <database-port>, <database-name>, <database-username>, and <database-password> with your own database details.
```
DB_HOST = "<database-host>"
DB_PORT = "<database-port>"
DB_NAME = "<database-name>"
DB_USER = "<database-username>"
DB_PASSWORD = "<database-password>"
```
4. Run the json_to_postgre.py script to insert the data from data.json into a PostgreSQL table.
```
python json_to_postgre.py
```

## Adiitional Notes
- You can customize the fields that are read from data.json and inserted into the PostgreSQL table by modifying the json_to_postgre.py script.
- If you need to modify the structure of the JSON data in data.json, you can use a tool like JSONLint to validate your JSON and ensure that it is properly formatted.
- Any doubt about how to use this script, please contact me at [Telegram](https://t.me/joao_rodrigues1).