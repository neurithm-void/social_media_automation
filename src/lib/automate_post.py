import os
import time
import pandas as pd
from src.lib.google_drive_api import Google_Drive_API

class Automate_Post:
    def __init__(self, file_url):
        self.file_url=file_url
        self.spreadsheet_sample_range ='Sheet1!A:G' #change if you want to add more spec while uploading
        self.spreadsheet_instance = Google_Drive_API(spreadsheet=True)
        self.creds=self.spreadsheet_instance.create_spreadsheet_api_token()
        self.spreadsheet_data = self.spreadsheet_instance.get_spreadsheet_data(self.file_url, self.spreadsheet_sample_range)
        #remember idx_list will contain -1th index, so whike using values[i] use values[i+1]

    def get_header_completion_status_idx(self):
        headers=self.spreadsheet_data[0] #headears are 1st row of spreadsheet
        uploaded_idx_list = [self.spreadsheet_data.index(x) for x in self.spreadsheet_data[1:] if x[0]!=''] #uompletion_status uploaded row
        unuploaded_idx_list = [self.spreadsheet_data.index(x) for x in self.spreadsheet_data[1:] if x[0]==''] #uompletion_status unuploaded row
        return self.spreadsheet_data, headers, uploaded_idx_list, unuploaded_idx_list

    def update_complition_status(self, index):
        actual_index=index+1
        self.completion_status_timestamp = [actual_index][0]=time.time() #update timestamp of particular index
        self.spreadsheet_instance.post_spreadsheet_update(actual_index, self.completion_status_timestamp) #just update timestance cell


    def make_instagram_post(self):
        pass

    def make_facebook_post(self):
        pass

    def make_twitter_post(self):
        pass

    def make_linked_in_post(self):
        pass

    