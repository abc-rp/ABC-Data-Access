# Rquired modules can typically be installed using:

# pip install --upgrade google-cloud-storage
# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth-oauthlib  

from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# The Service Account JSON file will be supplied once a data request is approved.

key_path = ""

credentialsSheets = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
)

credentialsBigQuery = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(
    credentials=credentialsBigQuery,
    project=credentialsBigQuery.project_id,
)

# The Google Sheet ID will be supplied once a data request is approved

SAMPLE_SPREADSHEET_ID = ''
SAMPLE_RANGE_NAME = 'A:G'
service = build('sheets', 'v4', credentials=credentialsSheets)
sheet = service.spreadsheets()
pointsData = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()
pointsDataValues = pointsData.get('values', [])

houseID = "Plot 1"

def getUUID(building, pointname, serves):
    for row in pointsDataValues:
        if row[2] == building:
            if row[4] == pointname:
                if row[5] == serves:
                    return ([row[0]])

def getData(building, pointname, serves):

    thisUUID = getUUID(building, pointname, serves)
    
    print("Found UUID in Sheet: ", thisUUID )

    # The correct Goolge BigQuery table ID will be supplied once a data request is approved
    
    query_job = client.query(
        """
        SELECT * FROM `udmi.telemetry_main` WHERE uuid = '""" + str(thisUUID[0]) + """'
        LIMIT 1"""
    )
    
    results = query_job.result() 

    for row in results:
        print("Returned value: ", row.presentvalue)

getData("Plot 1", 'air_temperature_sensor', 'LivingRoom')