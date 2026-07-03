import threading

from cli.commands import CLI
from scheduler.scheduler import AlarmScheduler
from services.alarm_service import AlarmService
from storage.json_storage import JsonStorage


def main():

    storage = JsonStorage("alarms.json")

    service = AlarmService(storage)

    scheduler = AlarmScheduler(service)

    thread = threading.Thread(target=scheduler.start, daemon=True)

    thread.start()

    cli = CLI(service)

    cli.menu()


if __name__ == "__main__":
    main()
