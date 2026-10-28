#!/usr/bin/python3
"""Export the TODO lists of all employees to one JSON file."""
import json
import requests


def export_all_to_json():
    """Export all tasks of all employees to todo_all_employees.json."""
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    data = {}
    for user in users:
        user_id = user.get("id")
        data[str(user_id)] = [
            {"username": user.get("username"),
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_all_to_json()
