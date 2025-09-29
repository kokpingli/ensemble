from dataclasses import dataclass
from enum import Enum

from .identifiers import Technique


class PerformanceQuality(Enum):
    STRUGGLING = "struggling"
    DEVELOPING = "developing"
    SOLID = "solid"
    EXPRESSIVE = "expressive"
    MASTERFUL = "masterful"


@dataclass(frozen=True)
class PerformanceMetrics:
    pitch_accuracy: float
    rhythm_stability: float
    dynamic_expression: float
    bow_smoothness: float
    attempted_technique: Technique
    performance_duration: float
    tempo_consistency: float
    overall_quality: PerformanceQuality
    confidence_level: float

    PRECISION_IMPORTANCE = 0.6
    RHYTHM_IMPORTANCE = 0.4
    EXPRESSION_IMPORTANCE = 0.5
    PRECISION_CONTRIBUTION = 0.3
    BOW_TECHNIQUE_IMPORTANCE = 0.2
    PRECISION_DELIGHT_THRESHOLD = 0.95
    EXPRESSION_DELIGHT_THRESHOLD = 0.8

    def calculate_precision_focused_satisfaction(self) -> float:
        return (
            self.pitch_accuracy * self.PRECISION_IMPORTANCE
            + self.rhythm_stability * self.RHYTHM_IMPORTANCE
        )

    def calculate_expression_focused_satisfaction(self) -> float:
        return (
            self.dynamic_expression * self.EXPRESSION_IMPORTANCE
            + self.pitch_accuracy * self.PRECISION_CONTRIBUTION
            + self.bow_smoothness * self.BOW_TECHNIQUE_IMPORTANCE
        )

    def meets_precision_delight_standards(self) -> bool:
        return self.pitch_accuracy >= self.PRECISION_DELIGHT_THRESHOLD

    def meets_expression_delight_standards(self) -> bool:
        return (
            self.calculate_expression_focused_satisfaction()
            >= self.EXPRESSION_DELIGHT_THRESHOLD
        )
