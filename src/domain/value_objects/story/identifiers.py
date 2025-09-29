from dataclasses import dataclass
from enum import Enum
from typing import NewType

WeaverId = NewType("WeaverId", str)
RealmId = NewType("RealmId", str)
SpiritId = NewType("SpiritId", str)
ChallengeId = NewType("ChallengeId", str)


class RealmType(Enum):
    BAROQUE = "baroque"
    CLASSICAL = "classical"
    ROMANTIC = "romantic"
    MODERN = "modern"


class Technique(Enum):
    MAJOR_SCALE = "major_scale"
    MINOR_SCALE = "minor_scale"
    ARPEGGIOS = "arpeggios"
    CHROMATIC_SCALE = "chromatic_scale"
    POSITION_SHIFTS = "position_shifts"
    VIBRATO = "vibrato"
    STACCATO = "staccato"
    LEGATO = "legato"
    HARMONICS = "harmonics"
    DOUBLE_STOPS = "double_stops"
    TREMOLO = "tremolo"
    SUL_PONTICELLO = "sul_ponticello"
    DYNAMICS = "dynamics"
    PHRASING = "phrasing"
    RUBATO = "rubato"
    ARTICULATION = "articulation"


class SpiritType(Enum):
    CLOCKWORK = "clockwork"
    MECHANICAL = "mechanical"
    ORNAMENTAL = "ornamental"
    NATURE = "nature"
    GARDEN = "garden"
    ELEMENTAL = "elemental"
    STORM = "storm"
    EMOTIONAL = "emotional"
    SKY = "sky"
    CIRCUIT = "circuit"
    INDUSTRIAL = "industrial"
    FUSION = "fusion"


@dataclass(frozen=True)
class TimePeriod:
    start_year: int
    end_year: int

    def __str__(self) -> str:
        return f"{self.start_year}-{self.end_year}"

    @classmethod
    def baroque(cls) -> "TimePeriod":
        return cls(1600, 1750)

    @classmethod
    def classical(cls) -> "TimePeriod":
        return cls(1750, 1820)

    @classmethod
    def romantic(cls) -> "TimePeriod":
        return cls(1820, 1900)

    @classmethod
    def modern(cls) -> "TimePeriod":
        return cls(1900, 2024)


class DifficultyLevel(Enum):
    NOVICE = "novice"
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    MASTER = "master"


class MasteryLevel(Enum):
    UNAWARE = "unaware"
    STRUGGLING = "struggling"
    DEVELOPING = "developing"
    COMPETENT = "competent"
    PROFICIENT = "proficient"
    MASTERFUL = "masterful"
