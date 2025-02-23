import os
import requests
import json

# OpenLoop Banner
banner = f"""
 ██████╗ ██████╗ ███████╗███╗   ██╗██╗      ██████╗  ██████╗ ██████╗ 
██╔════╝ ██╔══██╗██╔════╝████╗  ██║██║     ██╔═══██╗██╔═══██╗██╔══██╗
██║  ███╗██████╔╝█████╗  ██╔██╗ ██║██║     ██║   ██║██║   ██║██████╔╝
██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║   ██║██║   ██║██╔══██╗
╚██████╔╝██║     ███████╗██║ ╚████║███████╗╚██████╔╝╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                [  OPENLOOP API INTERFACE  ]                                                    
"""

print(banner)

# OpenLoop API Info
BASE_URL = "https://api.openloop.so"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ..."  # Replace with actual token

# User menu
print("Choose an option: ⭐️")
print("1. Check Bandwidth Info 📡")
print("2. Run Main OpenLoop Script 🔑")
choice = input("Enter your choice (1 or 2): ").strip()

# Function to fetch bandwidth info
def fetch_bandwidth_info():
    url = f"{BASE_URL}/bandwidth/info"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data, indent=4))  # Pretty print JSON response
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error fetching data: {e}")

# Function to run main OpenLoop script (simulating script execution)
def run_main_script():
    print("Running OpenLoop main script...")
    # Simulate main script logic here
    # Example: Making another API request or processing data

# Handle user choice
if choice == "1":
    fetch_bandwidth_info()
elif choice == "2":
    run_main_script()
else:
    print("Invalid choice. Please enter 1 or 2.")
