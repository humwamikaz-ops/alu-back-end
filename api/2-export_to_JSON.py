#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file using a REST API."""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export all tasks of a given employee to USER_ID.json.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(
        "{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}).json()

    username = user.get("username")

    data = {str(employee_id): [
        {"task": task.get("title"),
         "completed": task.get("completed"),
         "username": username}
        for task in todos
    ]}

    with open("{}.json".format(employee_id), "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    export_to_json(int(sys.argv[1]))
