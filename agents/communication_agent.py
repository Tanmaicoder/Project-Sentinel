class CommunicationAgent:

    def generate_alerts(self, severity):

        return {

            "public_alert":
                f"{severity} disaster detected. Move to safe zones immediately.",

            "emergency_sms":
                f"EMERGENCY ALERT: {severity} risk. Follow evacuation instructions.",

            "government_briefing":
                f"{severity} disaster situation requiring immediate response."
        }