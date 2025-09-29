from dataclasses import dataclass


@dataclass(frozen=True)
class SpiritCharacteristics:
    harmony_restoration: float
    encouragement_level: float

    @classmethod
    def nature_delighted(cls):
        return cls(harmony_restoration=0.7, encouragement_level=0.85)

    @classmethod
    def nature_concerned(cls):
        return cls(harmony_restoration=0.2, encouragement_level=0.6)
