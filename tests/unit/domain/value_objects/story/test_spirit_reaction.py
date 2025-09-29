from src.domain.value_objects.story.spirit_mood import SpiritMood
from src.domain.value_objects.story.spirit_reaction import SpiritReaction


class TestSpiritReaction:

    def test_delighted_factory_creates_positive_reaction(self):
        reaction = SpiritReaction.delighted("Great playing!", 0.9)

        assert reaction.spirit_mood.name == SpiritMood.DELIGHTED
        assert reaction.reaction_message == "Great playing!"
        assert reaction.creates_visual_effect is True
        assert reaction.offers_teaching_moment is False
        assert reaction.satisfaction_level == 0.9

    def test_concerned_factory_creates_teaching_reaction(self):
        reaction = SpiritReaction.concerned("Needs work", "Try practicing slowly", 0.4)

        assert reaction.spirit_mood.name == SpiritMood.CONCERNED
        assert reaction.reaction_message == "Needs work"
        assert reaction.teaching_advice == "Try practicing slowly"
        assert reaction.creates_visual_effect is False
        assert reaction.offers_teaching_moment is True
        assert reaction.satisfaction_level == 0.4

    def test_delighted_factory_uses_default_harmony_restoration(self):
        reaction = SpiritReaction.delighted("Excellent!", 0.95)

        assert (
            reaction.harmony_restoration
            == SpiritReaction.DEFAULT_DELIGHTED_HARMONY_RESTORATION
        )

    def test_concerned_factory_allows_custom_encouragement_level(self):
        custom_encouragement = 0.8
        reaction = SpiritReaction.concerned(
            "Almost there", "Keep trying", 0.6, encouragement_level=custom_encouragement
        )

        assert reaction.encouragement_level == custom_encouragement
