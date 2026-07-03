from dataclasses import asdict, dataclass


@dataclass
class Alarm:
    id: int
    time: str
    message: str
    triggered: bool = False

    def to_dict(self):
        return asdict(self)
