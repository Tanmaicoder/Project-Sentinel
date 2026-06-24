class ResourceAgent:

    def analyze(self, risk_score):

        return {
            "food_kits": risk_score * 500,
            "water_supply_liters": risk_score * 3000,
            "shelters": max(5, risk_score // 5)
        }