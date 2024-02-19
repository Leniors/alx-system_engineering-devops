#!/usr/bin/python3
"""
request an api
"""

if __name__ == "__main__":
    import json
    import random
    import requests
    import sys

    u_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"
    user = requests.get(user_url).json()

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
    todos = requests.get(todo_url).json()

    done = 0
    for todo in todos:
        if todo.get("completed"):
            done += 1

    print(
        f"Employee {user['name']} is done with tasks({done}/{len(todos)}):")

    for todo in todos:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")
