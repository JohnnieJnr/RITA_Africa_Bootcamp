import requests
import json

payload = {
    "name": "RITA Africa", 
    "language": "Python"
    
    }
url = "https://httpbin.org/post"
try:
    # Send the POST request with JSON data
    response = requests.post(url, json=payload)

    # Print the status code
    print(f"Status Code: {response.status_code}")

    # Print the response JSON
    print("Response JSON:")
    print(json.dumps(response.json(), indent=4))

except requests.exceptions.RequestException as err:
    print(f"Request error: {err}")

except Exception as err:
    print(f"An unexpected error occurred: {err}")

