# Google Analytics API Data Extraction and Storage

This Python script utilizes the Google Analytics API to access Google Analytics data. It fetches data from a specified Google Analytics account using Google credentials, processes the data, and stores it as a CSV file in a PostgreSQL database.

## Prerequisites

1. Python 3.x installed on your system.
2. Install required packages by running `pip install google-analytics-data google-auth google-auth-oauthlib google-auth-httplib2 pandas psycopg2`.

## Setup

1. Obtain Google Analytics API credentials:
   - Go to the [Google Developers Console](https://console.developers.google.com/).
   - Create a new project or select an existing one.
   - Enable the "Analytics Reporting API" for the project.
   - Create credentials: "Service Account" type.
   - Download the JSON credentials file and rename it to `credentials.json`.

2. Set up PostgreSQL database:
   - Install PostgreSQL on your system if you haven't already.
   - Create a new database and note down the database name, username, password, and host.

3. Place the `credentials.json` file in the same directory as the Python script.

## Configuration

Open the Python script and modify the following variables as per your environment:

```python
property_id = "YOUR-GOOGLE-ANALYTICS-PROPERTY-ID"
database_name = "YOUR-POSTGRES-DATABASE-NAME"
database_user = "YOUR-POSTGRES-USERNAME"
database_password = "YOUR-POSTGRES-PASSWORD"
database_host = "YOUR-POSTGRES-HOST"
```

## Running the Script

Run the Python script `google_analytics_data_extraction.py`:

```bash
python google_analytics_data_extraction.py
```

The script will fetch data from Google Analytics using the specified credentials and property ID. It will then process the data, convert it to a CSV file, and store it in the PostgreSQL database under the table "ga_data".

## CSV Output

The CSV output will be stored in the same directory as the script with the name `analytics_data.csv`.

## PostgreSQL Table

The script will create a table named "ga_data" in your PostgreSQL database (if it doesn't exist) and insert the data into this table.

## Important Notes

- Ensure that you have the necessary permissions to access the Google Analytics account and the PostgreSQL database.
- Always handle your credentials securely and avoid sharing them with unauthorized users.
- Make sure to comply with the terms of service and API usage policies of Google Analytics.

Feel free to explore and modify the script according to your specific requirements and data extraction needs. Happy coding!
