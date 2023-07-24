import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_analytics_data():
    # Load Service Account credentials from the JSON file
    credentials_path = 'C:/Users/user3/Downloads/opendata-214506-28bf7540053e.json'
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    # Build the Google Analytics Reporting API client
    analytics = build('analyticsreporting', 'v4', credentials=credentials)

    # Query parameters
    metric = {'expression': 'ga:pageviews'}
    date_range = {'start_date': '7daysAgo', 'end_date': 'today'}
    dimensions = []  # You can add dimensions if needed

    # Build the request with the dummy viewId parameter
    request = {
        'viewId': 'ga:123456789',  # Replace this with any dummy number
        'dateRanges': [date_range],
        'metrics': [metric],
        'dimensions': dimensions
    }

    try:
        # Execute the request and get the response
        response = analytics.reports().batchGet(body={'reportRequests': [request]}).execute()

        # Process the response and extract the data
        data = response['reports'][0]['data']['rows'][0]['metrics'][0]['values'][0]
        return int(data)
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    pageviews = get_analytics_data()
    if pageviews is not None:
        print(f"Pageviews in the last 7 days (Account & Property level): {pageviews}")
