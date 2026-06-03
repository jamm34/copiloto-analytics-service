class OpportunityService:

    def calculate_score(
        self,
        segment,
        purchase_probability,
        churn_probability,
        score
    ):

        opportunity = 0

        opportunity += (
            purchase_probability * 40
        )

        opportunity += (
            score * 0.40
        )

        opportunity += (
            (1 - churn_probability)
            * 20
        )

        if segment == "VIP":
            opportunity += 10

        elif segment == "LOYAL":
            opportunity += 5

        elif segment == "AT_RISK":
            opportunity += 15

        final_score = min(
            round(opportunity,2),
            100
        )

        return final_score