class ActionService:

    def get_action(
        self,
        segment,
        churn_probability,
        purchase_probability
    ):

        if segment == "NEW_LEAD":

            return {
                "recommended_action":
                    "FIRST_CONTACT",

                "sales_priority":
                    "MEDIUM"
            }

        if (
            churn_probability >= 0.70
            and
            purchase_probability <= 0.30
        ):

            return {
                "recommended_action":
                    "RECOVERY_CAMPAIGN",

                "sales_priority":
                    "URGENT"
            }

        if (
            segment == "VIP"
            and
            purchase_probability >= 0.70
        ):

            return {
                "recommended_action":
                    "UPSELL",

                "sales_priority":
                    "HIGH"
            }

        if (
            purchase_probability >= 0.70
        ):

            return {
                "recommended_action":
                    "PRIORITY_CONTACT",

                "sales_priority":
                    "HIGH"
            }

        return {

            "recommended_action":
                "FOLLOW_UP",

            "sales_priority":
                "MEDIUM"
        }