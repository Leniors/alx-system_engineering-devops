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

    json_file = f"{user['id']}.json"

    todos_list = []

    for todo in todos:
        todo_dic = {"task": todo['title'],
                    "completed": todo['completed'],
                    "username": user['username']}
        todos_list.append(todo_dic)

    dic = {str(user['id']): todos_list}

    with open(json_file, mode='w', newline='') as file:
        file.write(json.dumps(dic))
