from dataclasses import dataclass


@dataclass
class Segment:
    id: int = None
    name: str = None


@dataclass
class Segments:
    data = list()
