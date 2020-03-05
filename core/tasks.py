import json
import logging

from core import kepler_app
from core.task_data import tasks


@kepler_app.triggered_task(route="/workshop/tasks", method="GET")
def tasks_endpoint(event, context):
    logging.info("Displaying tasks")

    task_json = json.dumps(tasks)

    return task_json
