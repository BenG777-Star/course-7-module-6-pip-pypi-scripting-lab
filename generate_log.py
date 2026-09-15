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

    # Matches the exact textbook print requirement from your image
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    response = requests.get("https://typicode.com")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

    log_entries = ["User logged in", "User updated profile", "Report exported"]
    generate_log(log_entries)
