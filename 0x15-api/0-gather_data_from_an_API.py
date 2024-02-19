#!/usr/bin/python3
"""
request an api
"""

if __name__ == "__main__":
    import json
    import random
    import requests
    import sys

    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    user_json = requests.get(user_url)
    user = json.loads(user_json.text)

    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={sys.argv[1]}"
    todos_json = requests.get(todo_url)
    todos = json.loads(todos_json.text)

    done_todos = 0
    for todo in todos:
        if todo.get("completed") == True:
            done_todos += 1

    print(
        f"Employee {user['name']} is done with tasks({done_todos}/{len(todos)}):")

    for todo in todos:
        if todo.get("completed") == True:
            print(f"\t{todo.get('title')}")
