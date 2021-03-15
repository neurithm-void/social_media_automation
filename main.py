from src.lib.automate_post import Automate_Post
import os

def test(file_url=None):
    automation_process = Automate_Post(file_url=file_url)
    spreadsheet_data, headers, uploaded_idx_list, unuploaded_idx_list = automation_process.get_header_completion_status_idx()

    for idx in unuploaded_idx_list:
        caption = spreadsheet_data[idx][6]
        hashtags = spreadsheet_data[idx][6]
        ppt_link = spreadsheet_data[idx][6]
        ppt_text_content = spreadsheet_data[idx][6]
        ppt_image_video_content = spreadsheet_data[idx][6]
        social_media_platform_list = spreadsheet_data[idx][6]

        for platform in social_media_platform_list:
            if platform.find("instagram") != -1:
                automation_process.make_instagram_post()
            
            if platform.find("facebook") != -1:
                automation_process.make_facebook_post()
            
            if platform.find("twitter") != -1:
                automation_process.make_twitter_post()

            if platform.find("linkedin") != -1:
                automation_process.make_linked_in_post()
            
        automation_process.update_complition_status(idx) #update completion_status of a particular row


file_url="https://docs.google.com/spreadsheets/d/14lopq_gizMS5IxSSxb0HY1BP-vyBCG-OL27_rnDhaBc/edit?usp=sharing"
print(file_url)
test(file_url)
"""
if __name__=="main":
    file_url="https://docs.google.com/spreadsheets/d/14lopq_gizMS5IxSSxb0HY1BP-vyBCG-OL27_rnDhaBc/edit?usp=sharing"
    print(file_url)
"""