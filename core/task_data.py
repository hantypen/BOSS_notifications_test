
tasks = [
  {
    "external_id": "workshop-task-with-unique-number-after-this-string-301856",
    "description": "Example Task for a BOSS Workshop",
    "name": "BOSS Workshop Summary Task",
    "category": "Workshop Category 1",
    "assignee": {
      "type": "user",
      "email": "eric.mckibbin@datarobot.com"
    },
    "execution": {
      "type": "boss",
      "actions": [
        {
          "name": "OK",
          "type": "callback",
          "url": "https://boss.ngrok.io/slack/response?game=hearthstone"
        },
        {
          "name": "No",
          "type": "callback",
          "url": "https://boss.ngrok.io/slack/response?game=starcraft"
        }
      ]
    },
    "notifications": [
      {
        "type": "summary",
        "frequency": "daily",
        "delivery": {
          "type": "slack",
          "text": "Now you have a way to prototype and test BOSS tasks!"
        }
      }
    ]
  }
]
