# app/services/rule_service.py

from app.ml.thresholds import LOW_RISK, HIGH_RISK


class RuleService:

    def classify_risk(self, prob: float):

        if prob >= HIGH_RISK:
            return "HIGH"

        elif prob >= LOW_RISK:
            return "MEDIUM"

        return "LOW"

    def recommend_action(self, risk: str):

        actions = {
            "HIGH": "Offer discount + Retention call",
            "MEDIUM": "Send reminder email",
            "LOW": "No action needed"
        }

        return actions.get(risk, "No action")
