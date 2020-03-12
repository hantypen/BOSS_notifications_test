import json
import logging

from core import kepler_app
from core.task_data import tasks


@kepler_app.triggered_task(route="/workshop/tasks", method="GET")
def tasks_endpoint(event, context):
    logging.info("Displaying tasks")

    task_json = json.dumps(tasks)

    return task_json, 200, {'Content-Type': 'application/json'}


@kepler_app.triggered_task(route="/workshop/callback", method="POST")
def callback_endpoint(event, context):
    logging.info("Responding to callback", extra={"event": event})

    data = event.get('data')

    try:
        action = data['actions'][0]['name']
    except KeyError:
        response = {"message": "Sorry, still working on this :/"}
        return json.dumps(response), 200, {'Content-Type': 'application/json'}

    if action == 'OK':
        response = {"message": "Okay then"}
    elif action == 'No':
        response = {"message": "Oh... sorry :("}
    else:
        response = {"message": "Sorry, still working on this :/"}

    return json.dumps(response), 200, {'Content-Type': 'application/json'}
