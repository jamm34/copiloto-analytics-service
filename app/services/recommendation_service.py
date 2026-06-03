class RecommendationService:

    def get_recommendation(
        self,
        segment: str
    ):

        recommendations = {

            "VIP": {
                "priority": "HIGH",
                "recommendation": "Cliente de alto valor. Ofrecer venta cruzada y productos premium."
            },

            "LOYAL": {
                "priority": "HIGH",
                "recommendation": "Mantener seguimiento frecuente y ofrecer promociones exclusivas."
            },

            "ACTIVE": {
                "priority": "MEDIUM",
                "recommendation": "Mantener contacto comercial y presentar nuevos productos."
            },

            "OCCASIONAL": {
                "priority": "MEDIUM",
                "recommendation": "Incentivar nuevas compras con descuentos o promociones."
            },

            "AT_RISK": {
                "priority": "HIGH",
                "recommendation": "Cliente con riesgo de abandono. Contactar inmediatamente."
            },

            "NEW_LEAD": {
                "priority": "MEDIUM",
                "recommendation": "Primer contacto comercial. Presentar catálogo y promociones."
            }

        }

        return recommendations.get(
            segment,
            {
                "priority": "LOW",
                "recommendation": "Sin recomendación disponible."
            }
        )