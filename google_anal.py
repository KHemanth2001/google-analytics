import csv
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
path = DIR_PATH + folder_name
try:
    os.mkdir(path)
except OSError as error:
        print(error)


property_id = "353814524"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/user3/Downloads/automation-25cff4119eb3.json"

def format_date(date_str):
    # Assuming the input date_str is in the format "YYYYMMDD"
    # Convert it to "yyyy-mm-dd" format
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:]
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

def sample_run_report(property_id):
    """Runs a simple report on a Google Analytics 4 property."""
    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions=[Dimension(name="date")],
        metrics=[
            Metric(name="sessions"),
            Metric(name="screenPageViews"),
            Metric(name="eventCount"),
            Metric(name="userEngagementDuration"),
        ],
        date_ranges=[DateRange(start_date="2022-06-01", end_date="today")],
    )
    response = client.run_report(request)

    csv_filename = os.path.join(path, "analytics_report.csv")

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

sample_run_report(property_id)
