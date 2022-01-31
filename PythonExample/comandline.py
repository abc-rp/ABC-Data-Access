# Command line example, to retrieve the latest value for a given pointuid.
# To be used as: python3 commandline.py *pointuid*
# Example: python3 commandline.py 102eb94ae5c74f5c83c50ba78e43425a0

# Required modules can typically be installed using:

# pip install --upgrade google-cloud-storage
# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth-oauthlib  

import sys
from sty import bg, fg, rs
from google.cloud import storage
from google.cloud import bigquery
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# 

passed_uuid = sys.argv[1]


# The Service Account JSON file will be supplied once a data request is approved.

key_path = "** Path to provided JSON file **"


credentialsBigQuery = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(
    credentials=credentialsBigQuery,
    project=credentialsBigQuery.project_id,
)


def getData(uuid):
    
    # The correct Google BigQuery table ID will be supplied once a data request is approved
    
    query_job = client.query(
        """
        SELECT * FROM `** Provided BigQuery Table Path **` WHERE pointuid = '""" + passed_uuid + """' ORDER BY `timestamp` DESC
        LIMIT 1"""
    )
    
    results = query_job.result() 

    for row in results:
        a = fg.li_blue + str(row.timestamp) + rs.fg
        b = fg.li_blue + str(row.presentvalue) + rs.fg
        c = fg.li_blue + str(row.application) + rs.fg
        print(a)
        print(b )
        print(c)

getData(passed_uuid)