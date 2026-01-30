# app/services/decision_engine.py

from app.services.model_service import ModelService
from app.services.rule_service import RuleService


class DecisionEngine:

    def __init__(self):

        self.model_service = ModelService()
        self.rule_service = RuleService()

    def make_decision(self, features: list):

        prob = self.model_service.predict_probability(features)

        risk = self.rule_service.classify_risk(prob)

        action = self.rule_service.recommend_action(risk)

        return {
            "churn_probability": prob,
            "risk_level": risk,
            "recommended_action": action
        }
