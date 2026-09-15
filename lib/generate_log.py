import os
from datetime import datetime
# REQUIREMENT: Use import to bring in an external library
import requests

def generate_log(log_list):
    if not isinstance(log_list, list):
        raise ValueError("Input must be a list of log entries.")
        
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    with open(filename, "w") as file:
        for entry in log_list:
            file.write(f"{entry}\n")
            
    return filename

# REQUIREMENT: Wrap script logic inside the if __name__ == "__main__": block
if __name__ == "__main__":
    print("Fetching an entry from an external API using requests...")
    try:
        # Example of using the pip installed library to retrieve data
        response = requests.get("https://github.com", timeout=5)
        if response.status_code == 200:
            log_data = ["Automated check successful.", f"GitHub API Status: {response.status_code}"]
            created_file = generate_log(log_data)
            print(f"Success! Created file: {created_file}")
    except Exception as e:
        print(f"Could not connect to external API: {e}")
