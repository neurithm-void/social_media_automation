from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
import pandas as pd


class Google_Drive_API:

    def __init__(self, drive=False, spreadsheet=False):
        self.drive=drive
        self.spreadsheet=spreadsheet

        if self.drive: #https://developers.google.com/drive/api/v3/quickstart/python
            self.DRIVE_API_SCOPES = ['https://www.googleapis.com/auth/drive']

        if self.spreadsheet:
            self.SPREADSHEET_API_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        
        
    def create_spreadsheet_api_token(self):
        #https://developers.google.com/sheets/api/quickstart/python for any updates in api call for google spreadsheet api v4
        #run only once and before run make sure there's credential.json , you can generate one from the above link "enable api" uttonin cwd
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.SPREADSHEET_API_SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds


    def create_drive_api_token(self):
        #https://developers.google.com/drive/api/v3/quickstart/python for any updates in api call for google spreadsheet api v4
        #run only once and before run make sure there's credential.json , you can generate one from the above link "enable api" uttonin cwd
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', self.DRIVE_API_SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return creds

    def get_spreadsheet_as_dataframe(self, file_url, SAMPLE_RANGE_NAME = None):
        google_authetication_credentials = create_spreadsheet_api_token()
        file_id = file_url.split('//')[-1].split('/')[-2]
        service = build('sheets', 'v4', credentials=google_authetication_credentials)
        sheet = service.spreadsheets() 
        result = sheet.values().get(spreadsheetId=file_id,range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        headers=values[0] #headears are 1st row of spreadsheet
        data_rows=values[1:] #rest from 1st row will be considered as data_row

        df=pd.DataFrame(columns=headers, data=values[1:]) #creating dataframe

        return df

    def update_spreadsheet(self):
        pass