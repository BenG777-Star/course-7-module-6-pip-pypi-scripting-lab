import os
from datetime import datetime
import requests

def generate_log(log_list):
    if not isinstance(log_list, list):
        raise ValueError("Input must be a list of log entries.")
        
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    with open(filename, "w") as file:
        for entry in log_list:
            file.write(f"{entry}\n")
            
    # REQUIREMENT FIX: Print a confirmation message including the filename
    print(f"Log file created successfully: {filename}")
            
    return filename

if __name__ == "__main__":
    print("Fetching an entry from an external API using requests...")
    try:
        response = requests.get("https://github.com", timeout=5)
        if response.status_code == 200:
            log_data = ["Automated check successful.", f"GitHub API Status: {response.status_code}"]
            created_file = generate_log(log_data)
    except Exception as e:
        print(f"Could not connect to external API: {e}")
