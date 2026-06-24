class MedicalAgent:

    def analyze(self, risk_score):

        return {
            "ambulances": max(2, risk_score // 3),
            "doctors": max(5, risk_score // 2),
            "medical_kits": risk_score * 100
        }