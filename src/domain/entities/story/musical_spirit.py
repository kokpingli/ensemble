from abc import ABC, abstractmethod

from src.domain.value_objects.story.identifiers import SpiritType, Technique
from src.domain.value_objects.story.performance import PerformanceMetrics
from src.domain.value_objects.story.spirit_characteristics import \
    SpiritCharacteristics
from src.domain.value_objects.story.spirit_reaction import SpiritReaction


class MusicalSpirit(ABC):
    def __init__(self, name: str, spirit_type: SpiritType, primary_concern: Technique):
        self.name = name
        self.spirit_type = spirit_type
        self.primary_concern = primary_concern

    def react_to_performance(self, performance: PerformanceMetrics) -> SpiritReaction:
        satisfaction = self._calculate_satisfaction(performance)

        if self._meets_delight_standards(performance):
            return self._create_delighted_reaction(satisfaction)
        else:
            return self._create_concerned_reaction(satisfaction)

    @abstractmethod
    def _calculate_satisfaction(self, performance: PerformanceMetrics) -> float:
        pass

    @abstractmethod
    def _meets_delight_standards(self, performance: PerformanceMetrics) -> bool:
        pass

    @abstractmethod
    def _create_delighted_reaction(self, satisfaction: float) -> SpiritReaction:
        pass

    @abstractmethod
    def _create_concerned_reaction(self, satisfaction: float) -> SpiritReaction:
        pass


class ClockworkSpirit(MusicalSpirit):
    def __init__(self, name, primary_concern=Technique.MAJOR_SCALE):
        super().__init__(name, SpiritType.CLOCKWORK, primary_concern)

    @classmethod
    def create_chronos(cls):
        return cls("Chronos")

    def _calculate_satisfaction(self, performance: PerformanceMetrics) -> float:
        return performance.calculate_precision_focused_satisfaction()

    def _meets_delight_standards(self, performance: PerformanceMetrics) -> bool:
        return performance.meets_precision_delight_standards()

    def _create_delighted_reaction(self, satisfaction: float) -> SpiritReaction:
        return SpiritReaction.delighted(
            "Your precise notes awaken my clockwork heart!", satisfaction
        )

    def _create_concerned_reaction(self, satisfaction: float) -> SpiritReaction:
        return SpiritReaction.concerned(
            "The gears struggle with imprecise intonation",
            "Focus on careful intonation - each note must find its perfect place",
            satisfaction,
        )


class NatureSpirit(MusicalSpirit):
    def __init__(self, name, primary_concern=Technique.PHRASING):
        super().__init__(name, SpiritType.NATURE, primary_concern)

    def _calculate_satisfaction(self, performance: PerformanceMetrics) -> float:
        return performance.calculate_expression_focused_satisfaction()

    def _meets_delight_standards(self, performance: PerformanceMetrics) -> bool:
        return performance.meets_expression_delight_standards()

    def _create_delighted_reaction(self, satisfaction: float) -> SpiritReaction:
        characteristics = SpiritCharacteristics.nature_delighted()
        return SpiritReaction.delighted(
            "Your musical expression flows like a gentle stream!",
            satisfaction,
            harmony_restoration=characteristics.harmony_restoration,
            encouragement_level=characteristics.encouragement_level,
        )

    def _create_concerned_reaction(self, satisfaction: float) -> SpiritReaction:
        characteristics = SpiritCharacteristics.nature_concerned()
        return SpiritReaction.concerned(
            "The music needs more feeling, more life",
            "Try to put more expression and feeling into your playing",
            satisfaction,
            harmony_restoration=characteristics.harmony_restoration,
            encouragement_level=characteristics.encouragement_level,
        )
