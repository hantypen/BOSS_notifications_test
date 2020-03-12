import json
import logging

from core import kepler_app
from core.task_data import tasks


@kepler_app.triggered_task(route="/workshop/tasks", method="GET")
def tasks_endpoint(event, context):
    logging.info("Displaying tasks")

    task_json = json.dumps(tasks)

    return task_json


@kepler_app.triggered_task(route="/workshop/callback", method="POST")
def callback_endpoint(event, context):
    logging.info("Responding to callback", extra={"event": event})

    response = {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": "OK",
        "message": "test_message"
    }

    return response
