from google import genai
from dotenv import load_dotenv
import os
import json

from agents.evacuation_agent import EvacuationAgent
from agents.communication_agent import CommunicationAgent

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


class CoordinatorAgent:

    def coordinate(self, report):

        prompt = f"""
Return ONLY valid JSON.

{{
  "risk_assessment": {{
    "severity": "",
    "risk_score": 0,
    "major_threats": []
  }},
  "medical_response": {{
    "ambulances": 0,
    "doctors": 0,
    "medical_kits": 0
  }},
  "resource_allocation": {{
    "food_kits": 0,
    "water_supply_liters": 0,
    "shelters": 0
  }}
}}

Disaster Report:
{report}
"""

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            txt = response.text.strip()

            txt = txt.replace("```json", "")
            txt = txt.replace("```", "")
            txt = txt.strip()

            data = json.loads(txt)

        except Exception as e:

            print("Gemini Error:", e)
            print("Using fallback response...")

            data = {
                "risk_assessment": {
                    "severity": "CRITICAL",
                    "risk_score": 92,
                    "major_threats": [
                        "Severe Flooding",
                        "Road Blockage",
                        "Power Outages"
                    ]
                },
                "medical_response": {
                    "ambulances": 40,
                    "doctors": 60,
                    "medical_kits": 7500
                },
                "resource_allocation": {
                    "food_kits": 50000,
                    "water_supply_liters": 450000,
                    "shelters": 750
                }
            }

        # Run Evacuation Agent
        risk_score = data["risk_assessment"]["risk_score"]

        evacuation_plan = EvacuationAgent().analyze(
            risk_score
        )

        # Run Communication Agent
        severity = data["risk_assessment"]["severity"]

        communication = CommunicationAgent().generate_alerts(
            severity
        )

        # Add agent outputs
        data["evacuation_plan"] = evacuation_plan
        data["communication"] = communication

        return data