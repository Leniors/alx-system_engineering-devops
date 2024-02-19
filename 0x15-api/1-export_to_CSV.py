#!/usr/bin/python3
"""
request an api
"""

if __name__ == "__main__":
    import csv
    import json
    import random
    import requests
    import sys

    u_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"
    user = requests.get(user_url).json()

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
    todos = requests.get(todo_url).json()

    csv_file = f"{user['id']}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for todo in todos:
            row = [user['id'], user['username'], todo['completed'], todo['title']]
            writer.writerow(row)
