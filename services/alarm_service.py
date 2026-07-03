from models.alarm import Alarm


class AlarmService:

    def __init__(self, storage):
        self.storage = storage

    def get_all(self):
        """
        Display all stored alarms.

        Shows each alarm's ID, scheduled time, message, and current status.

        """
        return [Alarm(**a) for a in self.storage.load()]

    def add_alarm(self, time, message):
        """
        The method validates the entered time before delegating the
        creation of the alarm to the service layer.

        Returns:
            None
        """
        alarms = self.get_all()

        new_id = 1
        if alarms:
            new_id = max(a.id for a in alarms) + 1

        alarm = Alarm(new_id, time, message)

        alarms.append(alarm)

        self.storage.save([a.to_dict() for a in alarms])

    def delete_alarm(self, alarm_id):
        """
        Delete an existing alarm.

        Prompts the user for an alarm ID and removes the corresponding
        alarm if it exists.

        """

        alarms = self.get_all()

        if not any(alarm.id == alarm_id for alarm in alarms):
            print("Alarm not found")
            return False

        alarms = [a for a in alarms if a.id != alarm_id]

        self.storage.save([a.to_dict() for a in alarms])

        return True

    def mark_triggered(self, alarm_id):
        '''
        triggered Alarm and mark as done
        '''

        alarms = self.get_all()

        for alarm in alarms:
            if alarm.id == alarm_id:
                alarm.triggered = True

        self.storage.save([a.to_dict() for a in alarms])
