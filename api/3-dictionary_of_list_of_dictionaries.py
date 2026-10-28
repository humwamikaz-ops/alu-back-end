#!/usr/bin/python3
"""Export all employees' TODO lists to a single JSON file."""
import json
import requests
 
 
if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
 
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()
 
    data = {}
    for user in users:
        user_id = user.get("id")
        data[str(user_id)] = [
            {"username": user.get("username"),
             "task": t.get("title"),
             "completed": t.get("completed")}
            for t in todos if t.get("userId") == user_id
        ]
 
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
 
