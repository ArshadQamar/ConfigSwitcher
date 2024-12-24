import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def update_stream(toggle_payload):
    response = requests.post(url, auth=auth, json=toggle_payload)
    # Check the response status
    if response.status_code == 200:
        print("Stream configuration updated successfully:", response.json())
    else:
        print(f"Failed to update stream configuration. Status code: {response.status_code}")
        print("Response:", response.text)


#Fetching the variables
url=os.getenv("API_URL_CONTROL")
print(url)
auth=(os.getenv("API_USERNAME"), os.getenv("API_PASSWORD"))

#add the ids of the astra stream to toggle
#a015=dawn stream
#a014=khi stream
stream_ids = ["a015","a014"]

# Loop over each ID, set it in toggle_payload, and call update_stream
for stream_id in stream_ids:
    toggle_payload = {
        "cmd": "toggle-stream",
        "id": stream_id  # Set "id" to the current stream_id
    }
    update_stream(toggle_payload)