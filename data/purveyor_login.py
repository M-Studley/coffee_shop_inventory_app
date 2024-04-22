from dataclasses import dataclass


@dataclass
class PurveyorLogin:
    id: int
    name: str
    password: str
