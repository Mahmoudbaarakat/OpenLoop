import requests
import json
import time

# OpenLoop API Details
BASE_URL = "https://api.openloop.so"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ..."  # Replace with actual token
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json"
}

# Function to fetch bandwidth info
def fetch_bandwidth_info():
    url = f"{BASE_URL}/bandwidth/info"
    
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            print("✅ Bandwidth Info Retrieved Successfully!")
            return data
        else:
            print(f"❌ API Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error Fetching Data: {e}")
        return None

# Function to save data to a file
def save_to_file(data, filename="openloop_data.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print(f"📁 Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error Saving Data: {e}")

# Main Execution
if __name__ == "__main__":
    print("🔄 Fetching OpenLoop Bandwidth Info...")
    bandwidth_info = fetch_bandwidth_info()
    
    if bandwidth_info:
        save_to_file(bandwidth_info)
    else:
        print("⚠️ No data to save.")

    print("✅ OpenLoop Script Execution Completed!")
