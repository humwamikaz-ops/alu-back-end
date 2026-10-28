#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import requests
import sys


def display_progress(employee_id):
    """Print the TODO list progress of a given employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get(
        "{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}).json()

    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    display_progress(int(sys.argv[1]))
