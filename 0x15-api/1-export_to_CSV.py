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
    all_tasks = []

    for task in tasks_json:
        if int(id) == task.get('userId'):
            all_tasks.append(task)

    filename = "{}.csv".format(id)

    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            csv_writer.writerow([int(id), emp_name, task.get('completed'),
                                task.get('title')])
