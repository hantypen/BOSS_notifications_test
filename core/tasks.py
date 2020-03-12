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

    data = event.get('json', {}).get('body')

    response = {"message": "No Response Selected"}

    if data.get('response'):
        if data['response'] == 'ok':
            response = {"message": "Okay then"}
        elif data['response'] == 'no':
            response = {"message": "Oh... sorry :("}

    return json.dumps(response), 200, {'Content-Type': 'application/json'}
