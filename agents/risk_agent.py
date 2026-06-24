from ml.predict import predict_flood_risk

class RiskAgent:

    def analyze(
        self,
        rainfall,
        river_level,
        population_density
    ):

        prediction, probability = predict_flood_risk(
            rainfall,
            river_level,
            population_density
        )

        risk_score = int(probability)

        if risk_score >= 85:
            severity = "CRITICAL"
        elif risk_score >= 60:
            severity = "HIGH"
        elif risk_score >= 40:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        return {
            "severity": severity,
            "risk_score": risk_score,
            "major_threats": [
                "Flooding",
                "Infrastructure Damage",
                "Public Safety Risk"
            ]
        }