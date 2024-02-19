#!/usr/bin/python3
"""
request an api
"""

if __name__ == "__main__":
    import json
    import requests

    user_url = f"https://jsonplaceholder.typicode.com/users"
    users = requests.get(user_url).json()

    json_file = f"todo_all_employees.json"
    all_dic = {}

    for user in users:
        u_id = user['id']
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
        todos = requests.get(todo_url).json()

        todos_list = []

        for todo in todos:
            todo_dic = {"username": user['username'],
                        "task": todo['title'],
                        "completed": todo['completed']}
            todos_list.append(todo_dic)

        dic = {str(user['id']): todos_list}
        all_dic.update(dic)

    with open(json_file, mode='w', newline='') as file:
        file.write(json.dumps(all_dic))
