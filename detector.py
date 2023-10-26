import json
import sys
import os
from browser_history import get_history

outputs = get_history()
his = outputs.histories

current_directory = os.getcwd()
with open(current_directory + "/domains.json", 'r') as file:
    data = json.load(file)

domains = data.get("domains", [])

for domain in domains:
    if any(domain in word for word in his):
        print("I found something in your history!")
        sys.exit(1)