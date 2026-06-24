from agents.coordinator_agent import CoordinatorAgent
from agents.evacuation_agent import EvacuationAgent
from agents.communication_agent import CommunicationAgent
import json

report = """
Severe flooding reported near Hospet.

Population affected: 50,000

Heavy rainfall expected for next 72 hours.

Several roads are inaccessible.

Power outages reported.
"""

coordinator = CoordinatorAgent()

result = coordinator.coordinate(report)

# Additional agents
evac_agent = EvacuationAgent()
comm_agent = CommunicationAgent()

risk_score = result["risk_assessment"]["risk_score"]
severity = result["risk_assessment"]["severity"]

result["evacuation_plan"] = evac_agent.analyze(risk_score)
result["communication"] = comm_agent.generate_alerts(severity)

print(json.dumps(result, indent=4))