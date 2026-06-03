class ExplainabilityService:

    def explain_action(
        self,
        segment,
        churn_probability,
        purchase_probability,
        favorite_category
    ):

        reasons = []

        if segment == "VIP":
            reasons.append(
                "Cliente VIP."
            )

        if segment == "AT_RISK":
            reasons.append(
                "Cliente en riesgo de abandono."
            )

        if churn_probability >= 0.70:
            reasons.append(
                "Alta probabilidad de churn."
            )

        if purchase_probability >= 0.70:
            reasons.append(
                "Alta probabilidad de compra próxima."
            )

        if purchase_probability <= 0.30:
            reasons.append(
                "Baja probabilidad de compra próxima."
            )

        if favorite_category:
            reasons.append(
                f"Interés principal en {favorite_category}."
            )

        return " ".join(reasons)