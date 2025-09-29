from .spirit_mood import SpiritMood


class SpiritReaction:
    def __init__(
        self,
        spirit_mood,
        reaction_message,
        creates_visual_effect,
        harmony_restoration,
        offers_teaching_moment,
        teaching_advice,
        encouragement_level,
        satisfaction_level,
    ):
        self.spirit_mood = spirit_mood
        self.reaction_message = reaction_message
        self.creates_visual_effect = creates_visual_effect
        self.harmony_restoration = harmony_restoration
        self.offers_teaching_moment = offers_teaching_moment
        self.teaching_advice = teaching_advice
        self.encouragement_level = encouragement_level
        self.satisfaction_level = satisfaction_level

    DEFAULT_DELIGHTED_HARMONY_RESTORATION = 0.8
    DEFAULT_DELIGHTED_ENCOURAGEMENT = 0.9
    DEFAULT_CONCERNED_HARMONY_RESTORATION = 0.1
    DEFAULT_CONCERNED_ENCOURAGEMENT = 0.7

    @classmethod
    def delighted(
        cls,
        message,
        satisfaction,
        harmony_restoration=DEFAULT_DELIGHTED_HARMONY_RESTORATION,
        encouragement_level=DEFAULT_DELIGHTED_ENCOURAGEMENT,
    ):
        return cls(
            spirit_mood=SpiritMood(SpiritMood.DELIGHTED),
            reaction_message=message,
            creates_visual_effect=True,
            harmony_restoration=harmony_restoration,
            offers_teaching_moment=False,
            teaching_advice="",
            encouragement_level=encouragement_level,
            satisfaction_level=satisfaction,
        )

    @classmethod
    def concerned(
        cls,
        message,
        teaching_advice,
        satisfaction,
        harmony_restoration=DEFAULT_CONCERNED_HARMONY_RESTORATION,
        encouragement_level=DEFAULT_CONCERNED_ENCOURAGEMENT,
    ):
        return cls(
            spirit_mood=SpiritMood(SpiritMood.CONCERNED),
            reaction_message=message,
            creates_visual_effect=False,
            harmony_restoration=harmony_restoration,
            offers_teaching_moment=True,
            teaching_advice=teaching_advice,
            encouragement_level=encouragement_level,
            satisfaction_level=satisfaction,
        )
