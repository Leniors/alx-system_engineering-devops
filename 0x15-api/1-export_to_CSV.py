#!/usr/bin/python3
"""
request an api
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    u_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"
    user = requests.get(user_url).json()

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
    todos = requests.get(todo_url).json()

    csv_file = f"{user['id']}.csv"

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            user_id = user['id']
            username = user['username']
            todo_status = todo['completed']
            todo_title = todo['title']
            row = [user_id, username, todo_status, todo_title]
            writer.writerow(row)
