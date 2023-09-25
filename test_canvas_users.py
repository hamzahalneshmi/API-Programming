import json
import os
import requests
import sys

# network programming
BASE_URL = "https://canvas.ltu.se/api/v1"
COURSE_ID = 19899

# required Environment Variables
# CANVAS_TOKEN

# Get the value of the "token" environment variable
CANVAS_TOKEN = os.environ.get("CANVAS_TOKEN")

# Check if the variable is set
if CANVAS_TOKEN is None:
    print("CANVAS_TOKEN environment variable is not set.")
    sys.exit(1)
else:
    print("CANVAS_TOKEN: found")

headers = {
    "Authorization": "Bearer " + CANVAS_TOKEN,
}

response = requests.get(
    f"{BASE_URL}/courses/{COURSE_ID}/users",
    headers=headers)

print(response.status_code)

# Check if the response status code is 200 (OK) before attempting to parse the JSON response
if response.status_code != 200:
    print(f"Request failed with status code {response.status_code}")
    sys.exit(1)

users_data = response.json()

for user in users_data:

    # Pretty print the JSON data
    print(json.dumps(user, indent=4))

    # Access the 'name' key within each user dictionary
    # print(user['name'])

    # Access the 'sis_user_id' key within each user dictionary
    # print(user['sis_user_id'])

    # Access the 'sis_user_id' key within each user dictionary and verify that it is "maharg-3"
    if user['name'] == "Hamzah Murad Mohammed Al-Neshmi": # __________________________________________________________
        print(user['name'])
        sys.exit(0)

print("No user with sys_user_id 'maharg-3' found.")
sys.exit(1)
