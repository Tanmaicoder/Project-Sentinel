class EvacuationAgent:

    def analyze(self, risk_score):

        if risk_score >= 80:

            return {
                "evacuation_priority": "CRITICAL",
                "people_to_evacuate": risk_score * 200,
                "safe_locations": [
                    "Government School",
                    "Community Hall",
                    "Sports Stadium"
                ]
            }

        elif risk_score >= 50:

            return {
                "evacuation_priority": "HIGH",
                "people_to_evacuate": risk_score * 200,
                "safe_locations": [
                    "Government School",
                    "Community Hall"
                ]
            }

        else:

            return {
                "evacuation_priority": "LOW",
                "people_to_evacuate": risk_score * 200,
                "safe_locations": [
                    "Local Shelter"
                ]
            }