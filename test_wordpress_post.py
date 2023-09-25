import os
import sys
import requests

# required Environment Variables
# WP_USERNAME
# WP_KEY

# Get the value of the "WP_USERNAME" environment variable
WP_USERNAME = os.environ.get("WP_USERNAME")

# Check if the variable is set
if WP_USERNAME is None:
    print("WP_USERNAME environment variable is not set.")
    sys.exit(1)
else:
    print("WP_USERNAME: found")

# Get the value of the "WP_KEY" environment variable
WP_KEY = os.environ.get("WP_KEY")

# Check if the variable is set
if WP_KEY is None:
    print("WP_KEY environment variable is not set.")
    sys.exit(1)
else:
    print("WP_KEY: found")

# Define your credentials and base URL
BASE_URL = "https://toddbooth.com/wp-json/wp/v2"

# Define the post data as a dictionary
post_data = {
    "title": "Just A Random Post Title:Hamzah",# __________________________________________________________
    "content": "This is the content of the new post.",
    "status": "publish"
}

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Create the HTTP Basic Authentication string
auth_string = f"{WP_USERNAME}:{WP_KEY}"

# Send the POST request using the requests library
TIMEOUT_SECONDS = 5
response = requests.post(
    f"{BASE_URL}/posts/",
    auth=(WP_USERNAME, WP_KEY),
    headers=headers,
    json=post_data,
    timeout=TIMEOUT_SECONDS
)

# Check the response
if response.status_code == 201:
    print("Post created successfully!")
    sys.exit(0)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
    sys.exit(1)
