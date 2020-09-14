#!/usr/bin/python3
"""  using this REST API, for a given employee ID, returns
information about
 his/her TODO list progress"""


import requests
from sys import argv

if __name__ == "__main__":

    users_url = 'https://jsonplaceholder.typicode.com/users/{}'
    tasks_url = 'https://jsonplaceholder.typicode.com/todos'
    num_done_tasks = 0
    total_num_tasks = 0

    user_json = requests.get(users_url.format(argv[1])).json()
    tasks_json = requests.get(tasks_url).json()

    emp_name = user_json.get('name')
    tasks_done = []

    for task in tasks_json:
        if int(argv[1]) == task.get('userId'):
            total_num_tasks += 1
            if task.get('completed') is True:
                num_done_tasks += 1
                tasks_done.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, num_done_tasks, total_num_tasks))

    for task in tasks_done:
        print("\t {}".format(task))
