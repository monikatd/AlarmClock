import time
from datetime import datetime


class AlarmScheduler:

    def __init__(self, service):
        self.service = service

    def start(self):

        print("Scheduler started...")

        while True:

            now = datetime.now().strftime("%H:%M")

            alarms = self.service.get_all()

            for alarm in alarms:

                if not alarm.triggered and alarm.time == now:

                    print("\n")
                    print("********************************")
                    print(" ALARM ")
                    print(alarm.message)
                    print("********************************")
                    print()

                    self.service.mark_triggered(alarm.id)

            time.sleep(30)
