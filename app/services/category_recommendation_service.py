class CategoryRecommendationService:

    def get_category_recommendation(
        self,
        category_name: str
    ):

        recommendations = {

            "Laptops":
                "Ofrecer monitores, docking stations, SSD y accesorios premium.",

            "Smartphones":
                "Ofrecer auriculares, smartwatches, fundas y cargadores rápidos.",

            "Tablets":
                "Ofrecer stylus, teclados bluetooth, fundas y almacenamiento.",

            "Smartwatches":
                "Ofrecer auriculares, correas premium y accesorios deportivos.",

            "Auriculares":
                "Ofrecer DACs, smartwatches y dispositivos multimedia.",

            "Monitores":
                "Ofrecer laptops, teclados mecánicos y setups gaming.",

            "Teclados y Ratones":
                "Ofrecer monitores, mousepads premium y accesorios gaming.",

            "Almacenamiento":
                "Ofrecer SSD externos, NAS y upgrades de hardware."
        }

        return recommendations.get(
            category_name,
            "Sin recomendación específica disponible."
        )