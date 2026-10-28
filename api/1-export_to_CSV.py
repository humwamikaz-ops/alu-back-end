#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file using a REST API."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export all tasks of a given employee to USER_ID.csv.

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

    with open("{}.csv".format(employee_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])


if __name__ == "__main__":
    export_to_csv(int(sys.argv[1]))
