import csv
import psycopg2
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
folder_name = "\_Output"
filename = "analytics_report.csv"
path = os.path.join(DIR_PATH, folder_name)
try:
    os.mkdir(path)
except OSError as error:
    print(error)

property_id = "353814524"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/user3/Downloads/automation-25cff4119eb3.json"

def format_date(date_str):
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:8]
    hour = date_str[8:10]
    return f"{year}-{month.zfill(2)}-{day.zfill(2)} {hour}:00:00"

def sample_run_report(property_id):
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="dateHour")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
            Metric(name="eventCount"),
            Metric(name="userEngagementDuration"),
        ],
        date_ranges=[DateRange(start_date="2022-06-01", end_date="today")],
    )
    response = client.run_report(request)

    csv_filename = os.path.join(path, filename)

    print("Report result:")
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Sessions", "Screen Pageviews", "Event Count", "User Engagement Duration"])

        for row in response.rows:
            date = format_date(row.dimension_values[0].value)
            sessions = row.metric_values[0].value
            screen_pageviews = row.metric_values[1].value
            event_count = row.metric_values[2].value
            user_engagement_duration = row.metric_values[3].value

            writer.writerow([date, sessions, screen_pageviews, event_count, user_engagement_duration])

    print(f"Data has been saved to {csv_filename}")

def table(filename):
    conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='1234', port=5432)
    cur = conn.cursor()
    path = os.path.join(DIR_PATH, folder_name, filename)

    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS DATA(
     Date TIMESTAMP NOT NULL,
     sessions INTEGER,
     screenPageViews INTEGER,
     eventCount INTEGER,
     userEngagementDuration INTEGER)''')

    print("Table created")

    # Copy data from CSV
    sql2 = f'''COPY DATA(Date, Sessions, ScreenPageviews, EventCount, UserEngagementDuration)
    FROM '{path}'
    DELIMITER ','
    CSV HEADER;'''

    cur.execute(sql2)
    conn.commit()
    cur.close()
    conn.close()

print(filename)
sample_run_report(property_id)
table(filename)
