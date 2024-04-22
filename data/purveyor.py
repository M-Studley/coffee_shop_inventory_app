from dataclasses import dataclass


@dataclass
class Purveyor:
    id: int
    name: str
    url: str
    email: str
