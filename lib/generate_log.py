import os
from datetime import datetime

def generate_log(log_list):
    # 1. Test requires raising a ValueError if the input is not a list
    if not isinstance(log_list, list):
        raise ValueError("Input must be a list of log entries.")
        
    # 2. Test requires the filename format: log_YYYYMMDD.txt
    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"
    
    # 3. Create and write content to the file (handles empty list safely too)
    with open(filename, "w") as file:
        for entry in log_list:
            file.write(f"{entry}\n")
            
    # 4. CRITICAL: Must return the filename string to satisfy fixtures
    return filename
