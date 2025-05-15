import requests

try:
    responds = requests.get("https://randomfox.ca/floof/")
    
    # Check if request is successful
    if responds.status_code == 200:
        data = responds.json()
        print("Here's a random activity for you to complete now", data["image"])
        print("Source: ", data["link"])
    else:
        print("Failed to fetch activity")

except Exception as e:
    print("An error occurred")

