from datetime import datetime
import pytz
import time
from instagrapi import Client

# Define the IST timezone
ist = pytz.timezone('Asia/Kolkata')

api = Client()
# api.login("adhirajranjan_", "")

# api.dump_settings("adhirajranjan_.json")
# exit(0)

api.load_settings("adhirajranjan_.json")
api.get_timeline_feed() # check session

print("Logged in!")

recorded_date = None

while True:
    
    c_date = datetime.now(ist).day

    if c_date != recorded_date:
        api.account_change_picture(f'images/{c_date}.jpg')
        
        print(f"Profile updated at {c_date} day of this month")
        
        recorded_date = c_date

    time.sleep(3600)