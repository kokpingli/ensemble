from src.domain.value_objects.story.identifiers import Technique
from src.domain.value_objects.story.performance import (PerformanceMetrics,
                                                        PerformanceQuality)


class TestPerformanceMetrics:

    def test_precision_focused_satisfaction_weighs_pitch_accuracy_more_heavily(self):
        performance = PerformanceMetrics(
            pitch_accuracy=0.9,
            rhythm_stability=0.6,
            dynamic_expression=0.5,
            bow_smoothness=0.5,
            attempted_technique=Technique.MAJOR_SCALE,
            performance_duration=8.0,
            tempo_consistency=0.8,
            overall_quality=PerformanceQuality.SOLID,
            confidence_level=0.8,
        )

        satisfaction = performance.calculate_precision_focused_satisfaction()

        expected = 0.9 * 0.6 + 0.6 * 0.4  # 0.78
        assert abs(satisfaction - expected) < 0.001

    def test_expression_focused_satisfaction_weighs_dynamics_most_heavily(self):
        performance = PerformanceMetrics(
            pitch_accuracy=0.7,
            rhythm_stability=0.7,
            dynamic_expression=0.9,
            bow_smoothness=0.8,
            attempted_technique=Technique.PHRASING,
            performance_duration=10.0,
            tempo_consistency=0.75,
            overall_quality=PerformanceQuality.EXPRESSIVE,
            confidence_level=0.85,
        )

        satisfaction = performance.calculate_expression_focused_satisfaction()

        expected = 0.9 * 0.5 + 0.7 * 0.3 + 0.8 * 0.2  # 0.82
        assert abs(satisfaction - expected) < 0.001

    def test_meets_precision_standards_returns_true_for_high_pitch_accuracy(self):
        performance = PerformanceMetrics(
            pitch_accuracy=0.96,
            rhythm_stability=0.8,
            dynamic_expression=0.6,
            bow_smoothness=0.7,
            attempted_technique=Technique.MAJOR_SCALE,
            performance_duration=8.0,
            tempo_consistency=0.9,
            overall_quality=PerformanceQuality.EXPRESSIVE,
            confidence_level=0.9,
        )

        assert performance.meets_precision_delight_standards() is True

    def test_meets_precision_standards_returns_false_for_low_pitch_accuracy(self):
        performance = PerformanceMetrics(
            pitch_accuracy=0.85,
            rhythm_stability=0.9,
            dynamic_expression=0.8,
            bow_smoothness=0.9,
            attempted_technique=Technique.MAJOR_SCALE,
            performance_duration=8.0,
            tempo_consistency=0.95,
            overall_quality=PerformanceQuality.SOLID,
            confidence_level=0.85,
        )

        assert performance.meets_precision_delight_standards() is False
