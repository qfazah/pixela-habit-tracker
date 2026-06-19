from datetime import datetime
import os
import requests

# --- Configuration & Credentials ---
TOKEN = os.getenv("YOURS_TOKEN")
USER_NAME = "fazah"

# API Endpoints
REGISTER_END_POINT = "https://pixe.la/v1/users"
GRAPH_END_POINT = f"{REGISTER_END_POINT}/{USER_NAME}/graphs"
PIXEL_ADD_ENDPOINT = f"{REGISTER_END_POINT}/{USER_NAME}/graphs/myprojectgraph1"

# --- 1. User Registration ---
registration_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

print("Registering user...")
registration_response = requests.post(
    REGISTER_END_POINT, json=registration_params
)
print(f"Registration Status: {registration_response.json()}\n")

# --- 2. Graph Creation ---
auth_header = {"X-USER-TOKEN": TOKEN}

graph_config = {
    "id": "myprojectgraph1",
    "name": "Coding Tracker",
    "unit": "hr",
    "type": "float",
    "color": "shibafu",
    "description": "This is my coding graph that tracks how much time I spend on coding",
}

print("Creating graph...")
graph_response = requests.post(
    url=GRAPH_END_POINT, headers=auth_header, json=graph_config
)
print(f"Graph Status: {graph_response.json()}\n")

# --- 3. Pixel Logging ---
target_date = datetime(year=2026, month=6, day=15)

pixel_data = {
    "date": target_date.strftime("%Y%m%d"),
    "quantity": "30",
}

print(f"Adding pixel for {pixel_data['date']}...")
pixel_request = requests.post(
    PIXEL_ADD_ENDPOINT, headers=auth_header, json=pixel_data
)
print(f"Pixel Status: {pixel_request.json()}\n")

# --- View Results ---
# Dashboard Link: https://pixe.la/v1/users/fazah/graphs/myprojectgraph1.html
print("Execution complete. Check your dashboard link above!")