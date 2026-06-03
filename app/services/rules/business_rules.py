class BusinessRules:

    @staticmethod
    def get_customer_status(
        days_since_last_purchase
    ):

        if days_since_last_purchase is None:
            return "NEW_LEAD"

        if days_since_last_purchase > 180:
            return "LOST"

        if days_since_last_purchase > 90:
            return "AT_RISK"

        return "ACTIVE"

    @staticmethod
    def apply_segment_override(
        segment,
        days_since_last_purchase
    ):

        if (
            days_since_last_purchase
            and
            days_since_last_purchase > 180
        ):
            return "LOST"

        if (
            days_since_last_purchase
            and
            days_since_last_purchase > 90
        ):
            return "AT_RISK"

        return segment

    @staticmethod
    def generate_churn_label(
        days_since_last_purchase
    ):

        if (
            days_since_last_purchase
            and
            days_since_last_purchase > 90
        ):
            return 1

        return 0