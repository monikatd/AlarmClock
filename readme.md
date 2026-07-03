# CLI Alarm Clock

A command-line alarm clock application written in Python.

## Features

- Add alarms
- List alarms
- Delete alarms
- JSON-based persistent storage
- Background scheduler
- Input validation
- Graceful error handling

---

## Project Structure

```text
alarm_clock/
│
├── main.py
├── alarms.json
├── README.md
├── requirements.txt
│
├── cli/
│   └── commands.py
│
├── models/
│   └── alarm.py
│
├── services/
│   └── alarm_service.py
│
├── storage/
│   └── json_storage.py
│
└── scheduler/
    └── scheduler.py
```

---


## Requirements

- Python 3.10+

## Installation

git clone https://github.com/monikatd/AlarmClock.git

cd AlarmClock


## Run

python main.py

## Architecture

CLI
    ↓
Service
    ↓
Storage
    ↓
JSON File

Scheduler runs in a background thread and checks alarms every second.

