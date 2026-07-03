import json
import os


class JsonStorage:

    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save(self, alarms):
        with open(self.filename, "w") as f:
            json.dump(alarms, f, indent=4)
