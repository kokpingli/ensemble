from src.domain.entities.story.musical_spirit import (ClockworkSpirit,
                                                      NatureSpirit)
from src.domain.value_objects.story.identifiers import Technique
from src.domain.value_objects.story.performance import (PerformanceMetrics,
                                                        PerformanceQuality)


class TestSpiritReactions:

    def test_clockwork_spirit_delights_when_scale_has_95_percent_accuracy(self):
        chronos = ClockworkSpirit.create_chronos()

        excellent_scale_performance = PerformanceMetrics(
            pitch_accuracy=0.95,
            rhythm_stability=0.92,
            dynamic_expression=0.7,
            bow_smoothness=0.85,
            attempted_technique=Technique.MAJOR_SCALE,
            performance_duration=8.0,
            tempo_consistency=0.9,
            overall_quality=PerformanceQuality.EXPRESSIVE,
            confidence_level=0.88,
        )

        reaction = chronos.react_to_performance(excellent_scale_performance)

        assert reaction.spirit_mood.name == "DELIGHTED"
        assert "precise" in reaction.reaction_message.lower()
        assert reaction.creates_visual_effect is True
        assert reaction.harmony_restoration > 0

    def test_clockwork_spirit_offers_intonation_guidance_when_pitch_accuracy_below_70_percent(
        self,
    ):
        chronos = ClockworkSpirit.create_chronos()

        struggling_performance = PerformanceMetrics(
            pitch_accuracy=0.60,
            rhythm_stability=0.85,
            dynamic_expression=0.65,
            bow_smoothness=0.70,
            attempted_technique=Technique.MAJOR_SCALE,
            performance_duration=10.0,
            tempo_consistency=0.80,
            overall_quality=PerformanceQuality.STRUGGLING,
            confidence_level=0.45,
        )

        reaction = chronos.react_to_performance(struggling_performance)

        assert reaction.spirit_mood.name == "CONCERNED"
        assert reaction.offers_teaching_moment is True
        assert "intonation" in reaction.teaching_advice.lower()
        assert reaction.encouragement_level > 0.5

    def test_clockwork_spirit_cares_more_about_precision_than_nature_spirit_cares_about_expression(
        self,
    ):
        clockwork_spirit = ClockworkSpirit("Precision Pete")
        nature_spirit = NatureSpirit("Harmony Holly")

        high_precision_low_expression_performance = PerformanceMetrics(
            pitch_accuracy=0.95,
            rhythm_stability=0.94,
            dynamic_expression=0.65,
            bow_smoothness=0.80,
            attempted_technique=Technique.MAJOR_SCALE,
            performance_duration=8.0,
            tempo_consistency=0.92,
            overall_quality=PerformanceQuality.SOLID,
            confidence_level=0.80,
        )

        clockwork_reaction = clockwork_spirit.react_to_performance(
            high_precision_low_expression_performance
        )
        nature_reaction = nature_spirit.react_to_performance(
            high_precision_low_expression_performance
        )

        assert (
            clockwork_reaction.satisfaction_level > nature_reaction.satisfaction_level
        )
        assert (
            "expression" in nature_reaction.teaching_advice.lower()
            or "feeling" in nature_reaction.teaching_advice.lower()
        )
