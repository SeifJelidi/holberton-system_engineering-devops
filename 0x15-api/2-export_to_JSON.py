#!/usr/bin/python3
"""Using what you did in the task #0, extend your
Python script to export data in the JSON format"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    id = argv[1]
    users_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'

    user_json = requests.get(users_url).json()
    tasks_json = requests.get(tasks_url).json()

    emp_name = user_json.get('username')

    tasks_by_userid = {}
    task_list = []
    for task in tasks_json:
        task_json = {}
        if int(id) == task.get('userId'):
            task_json = {}
            task_json["task"] = task.get('title')
            task_json["completed"] = task.get('completed')
            task_json["username"] = emp_name
            task_list.append(task_json)

    tasks_by_userid[id] = task_list
    filename = "{}.json".format(id)

    with open(filename, 'w') as file:
        json.dump(tasks_by_userid, file)
