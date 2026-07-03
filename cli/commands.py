from datetime import datetime


class CLI:
    """
    Command-line interface for the Alarm Clock application.

    This class is responsible for interacting with the user by displaying
    menus, collecting input, validating data, and delegating business logic
    to the AlarmService.

    Attributes:
        service: Instance of AlarmService used to manage alarms.
    """

    def __init__(self, service):
        self.service = service

    def validate_time(self, value):
        """
        Validate a time string.

        Checks whether the provided time follows the 24-hour HH:MM format.

        Args:
            value (str): Time entered by the user.

        Returns:
            bool: True if the time is valid, otherwise False.
        """

        try:
            datetime.strptime(value, "%H:%M")
            return True
        except ValueError:
            return False

    def menu(self):

        while True:

            print("\nAlarm Clock")
            print("1. Add Alarm")
            print("2. List Alarms")
            print("3. Delete Alarm")
            print("4. Exit")

            choice = input("Choice: ")

            if choice == "1":

                alarm_time = input("Time (HH:MM): ")

                if not self.validate_time(alarm_time):
                    print("Invalid time format.")
                    continue

                message = input("Message: ")

                self.service.add_alarm(alarm_time, message)

                print("Alarm added.")

            elif choice == "2":

                alarms = self.service.get_all()

                if not alarms:
                    print("No alarms.")
                    continue

                for alarm in alarms:

                    status = "Done" if alarm.triggered else "Pending"

                    print(f"{alarm.id} | {alarm.time} | {alarm.message} | {status}")

            elif choice == "3":

                try:
                    alarm_id = int(input("Alarm ID: "))
                    if self.service.delete_alarm(alarm_id):
                        print("Deleted.")
                except ValueError:
                    print("Invalid ID.")

            elif choice == "4":
                break

            else:
                print("Invalid choice.")
