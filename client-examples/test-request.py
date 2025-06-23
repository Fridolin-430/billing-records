import requests

BILLING_ID = "sample-record-id"
API_URL = "https://<your-function-app-name>.azurewebsites.net/api/billing/{BILLING_ID}"

response = requests.get(API_URL)
print("Status Code:", response.status_code)
print("Response:", response.json())
