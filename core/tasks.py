import json
import logging

from core import kepler_app


@kepler_app.triggered_task(route="/workshop/tasks", method="GET")
def tasks_endpoint(event, context):
    logging.info("Displaying tasks")
    with open("tasks.json") as fp:
        data = fp.read()

    task_json = json.loads(data)

    return task_json
