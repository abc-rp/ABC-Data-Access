# Command line example, to retrieve all entries from META Google Sheet
# To be used as: python3 listmeta.py *Google Sheet ID*
# Example: python3 listmeta.py 1qXDpIRn_3Ifk1EfNWkHtnyz2tk_mach6cRPDF_9iBPQ

# Required modules can typically be installed using:

# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth-oauthlib  

import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build


passed_google_sheet_id = sys.argv[1]

# The Service Account JSON file will be supplied once a data request is approved.

key_path = "** Path to provided JSON file **"

credentialsSheets = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
)


SAMPLE_SPREADSHEET_ID = passed_google_sheet_id
SAMPLE_RANGE_NAME = 'A:G'
service = build('sheets', 'v4', credentials=credentialsSheets)
sheet = service.spreadsheets()
pointsData = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
pointsDataValues = pointsData.get('values', [])

houseID = "Plot 1"

for row in pointsDataValues:
    print(row)