#!/usr/bin/python3
""" Using what you did in the task #0, extend your
Python script to export data in the CSV format"""

import csv
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'

    user_json = requests.get(users_url).json()
    tasks_json = requests.get(tasks_url).json()

    emp_name = user_json.get('name')

    task_list = []
    for task in tasks_json:
        if int(id) == task.get('userId'):
            row = {}
            row["USER_ID"] = id
            row["USERNAME"] = emp_name
            row["TASK_COMPLETED_STATUS"] = task.get('completed')
            row["TASK_TITLE"] = task.get('title')
            task_list.append(row)

    filename = "{}.csv".format(id)
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)
        csv_writer.writerows(task_list)
