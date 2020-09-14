#!/usr/bin/python3
"""  using this REST API, for a given employee ID, returns
information about
 his/her TODO list progress"""


import requests
import csv
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'
    num_done_tasks = 0
    total_num_tasks = 0

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
